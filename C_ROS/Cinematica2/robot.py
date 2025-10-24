# robot.py
import numpy as np

class PlanarManipulator:
    """
    Representa un manipulador planar de 3 eslabones (3-GDL).
    Maneja los cálculos de cinemática y mantiene su estado actual
    para elegir la solución de movimiento mínimo.
    """

    def __init__(self, link_lengths):
        if len(link_lengths) != 3:
            raise ValueError("Se requieren exactamente 3 longitudes de eslabón.")
        self.link_lengths = np.array(link_lengths)
        self.n_links = len(link_lengths)
        self.max_reach = np.sum(self.link_lengths)
        
        # Posición inicial "Home" (45°, 45°, 0°)
        self.home_angles = np.array([np.pi/4, np.pi/4, 0])
        self.current_angles = self.home_angles

    def get_home_angles(self):
        """Devuelve los ángulos de la posición inicial."""
        return self.home_angles

    def set_current_angles(self, angles):
        """Actualiza el estado actual del robot."""
        self.current_angles = np.array(angles)

    def _shortest_angle_diff(self, a1, a2):
        """Calcula la diferencia más corta entre dos ángulos en radianes."""
        diff = a1 - a2
        # Mapea la diferencia al rango [-pi, pi]
        return (diff + np.pi) % (2 * np.pi) - np.pi

    def choose_best_solution(self, sol_up, sol_down):
        """
        Dadas dos soluciones, elige la que esté "más cerca"
        de los ángulos actuales del robot.
        """
        current = self.current_angles
        
        # Calcular el "costo" (distancia total de articulaciones) para la solución "arriba"
        cost_up = np.sum([
            abs(self._shortest_angle_diff(sol_up[i], current[i])) 
            for i in range(self.n_links)
        ])
        
        # Calcular el "costo" para la solución "abajo"
        cost_down = np.sum([
            abs(self._shortest_angle_diff(sol_down[i], current[i]))
            for i in range(self.n_links)
        ])
        
        # Elegir la solución con el costo más bajo
        if cost_up <= cost_down:
            return sol_up, "Codo Arriba"
        else:
            return sol_down, "Codo Abajo"


    # --- MÉTODOS DE CINEMÁTICA (Sin cambios) ---

    def _create_transform_matrix(self, q_rad, l):
        cos_q = np.cos(q_rad)
        sin_q = np.sin(q_rad)
        return np.array([
            [cos_q, -sin_q, l * cos_q],
            [sin_q,  cos_q, l * sin_q],
            [0,      0,     1]
        ])

    def direct_kinematics(self, angles):
        t1, t2, t3 = angles
        l1, l2, l3 = self.link_lengths
        
        p_origin = np.array([0, 0, 1])
        T1 = self._create_transform_matrix(t1, l1)
        p1 = T1 @ p_origin
        
        T2 = self._create_transform_matrix(t2, l2)
        T_1_2 = T1 @ T2
        p2 = T_1_2 @ p_origin
        
        T3 = self._create_transform_matrix(t3, l3)
        T_1_3 = T_1_2 @ T3
        p3 = T_1_3 @ p_origin

        return [
            (0, 0), (p1[0], p1[1]), (p2[0], p2[1]), (p3[0], p3[1])
        ]

    def inverse_kinematics(self, x_target, y_target, phi_target):
        l1, l2, l3 = self.link_lengths
        x_wrist = x_target - l3 * np.cos(phi_target)
        y_wrist = y_target - l3 * np.sin(phi_target)

        D_sq = x_wrist**2 + y_wrist**2
        D = np.sqrt(D_sq)

        if D > l1 + l2 or D < abs(l1 - l2) or D == 0:
            return None, None
        
        cos_t2 = (D_sq - l1**2 - l2**2) / (2 * l1 * l2)
        cos_t2 = np.clip(cos_t2, -1.0, 1.0) 
        
        sin_t2_up = np.sqrt(1 - cos_t2**2) 
        sin_t2_down = -sin_t2_up

        t2_up = np.arctan2(sin_t2_up, cos_t2)
        t2_down = np.arctan2(sin_t2_down, cos_t2)

        solutions = []
        for t2, sin_t2 in [(t2_up, sin_t2_up), (t2_down, sin_t2_down)]:
            k1 = l1 + l2 * cos_t2
            k2 = l2 * sin_t2
            t1 = np.arctan2(y_wrist, x_wrist) - np.arctan2(k2, k1)
            t3 = phi_target - t1 - t2
            
            # Normalizar para consistencia
            t1 = np.arctan2(np.sin(t1), np.cos(t1))
            t2 = np.arctan2(np.sin(t2), np.cos(t2))
            t3 = np.arctan2(np.sin(t3), np.cos(t3))
            
            solutions.append([t1, t2, t3])

        return solutions[0], solutions[1]
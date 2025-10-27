import numpy as np

class PlanarManipulator:
    """
    Representa un manipulador planar de 3 eslabones (3-GDL) (RRR).
    Maneja los cálculos de cinemática directa y cinemática inversa
    (numérica) y mantiene su estado actual.
    """

    def __init__(self, link_lengths):
        """
        Inicializa el robot con las longitudes de sus eslabones.
        
        Args:
            link_lengths (list or tuple): Una lista de 3 longitudes [l1, l2, l3].
        """
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
        """Actualiza el estado actual (ángulos) del robot."""
        self.current_angles = np.array(angles)

    # --- MÉTODOS DE CINEMÁTICA ---

    def _create_transform_matrix(self, q_rad, l):
        """Crea una matriz de transformación homogénea."""
        cos_q = np.cos(q_rad)
        sin_q = np.sin(q_rad)
        return np.array([
            [cos_q, -sin_q, l * cos_q],
            [sin_q,  cos_q, l * sin_q],
            [0,      0,     1]
        ])

    def direct_kinematics(self, angles):
        """
        Calcula la cinemática directa.
        Devuelve las posiciones (x, y) de todas las articulaciones.
        """
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

    # --- MÉTODOS DE CINEMÁTICA INVERSA NUMÉRICA (Newton-Raphson) ---
    
    def _calculate_F(self, angles, target_pose):
        """
        Calcula el vector de error F(q) para el método de Newton-Raphson.
        F(q) = [f_actual - f_deseado]
        """
        t1, t2, t3 = angles
        l1, l2, l3 = self.link_lengths
        x_t, y_t, phi_t = target_pose
        
        t12 = t1 + t2
        t123 = t1 + t2 + t3
        
        # Ecuaciones de cinemática directa
        pos_x = l1 * np.cos(t1) + l2 * np.cos(t12) + l3 * np.cos(t123)
        pos_y = l1 * np.sin(t1) + l2 * np.sin(t12) + l3 * np.sin(t123)
        pos_phi = t123
        
        # Vector de error
        f1 = pos_x - x_t
        f2 = pos_y - y_t
        f3 = pos_phi - phi_t
        
        # Normalizar el error del ángulo (f3) al rango [-pi, pi]
        f3 = (f3 + np.pi) % (2 * np.pi) - np.pi
        
        return np.array([f1, f2, f3])

    def _calculate_jacobian(self, angles):
        """
        Calcula la matriz Jacobiana J(q) para el método de Newton-Raphson.
        J(i, j) = d(f_i) / d(theta_j)
        """
        t1, t2, t3 = angles
        l1, l2, l3 = self.link_lengths
        
        s1 = np.sin(t1)
        c1 = np.cos(t1)
        s12 = np.sin(t1 + t2)
        c12 = np.cos(t1 + t2)
        s123 = np.sin(t1 + t2 + t3)
        c123 = np.cos(t1 + t2 + t3)
        
        J = np.zeros((3, 3))
        
        # Fila 1: d(f1) / d(theta_j)  (derivadas de pos_x)
        J[0, 0] = -l1 * s1 - l2 * s12 - l3 * s123
        J[0, 1] = -l2 * s12 - l3 * s123
        J[0, 2] = -l3 * s123
        
        # Fila 2: d(f2) / d(theta_j)  (derivadas de pos_y)
        J[1, 0] = l1 * c1 + l2 * c12 + l3 * c123
        J[1, 1] = l2 * c12 + l3 * c123
        J[1, 2] = l3 * c123
        
        # Fila 3: d(f3) / d(theta_j)  (derivadas de pos_phi)
        J[2, 0] = 1
        J[2, 1] = 1
        J[2, 2] = 1
        
        return J

    def inverse_kinematics(self, x_target, y_target, phi_target,
                           initial_guess="current",
                           max_iter=100, tolerance=1e-6, min_iter=5):
        """
        Calcula la cinemática inversa usando el método numérico de Newton-Raphson.
        Encuentra la solución más "cercana" a la estimación inicial.
        
        Args:
            x_target (float): Coordenada X deseada.
            y_target (float): Coordenada Y deseada.
            phi_target (float): Orientación final deseada (radianes).
            initial_guess (str or np.array):
                - "current" (default): Usa self.current_angles (ideal para trayectorias).
                - "random": Usa valores aleatorios [0, 1] rad (como en el PDF).
                - np.array: Un vector de 3 ángulos para usar como inicio.
            max_iter (int): Iteraciones máximas antes de fallar.
            tolerance (float): Umbral de error para convergencia.
            min_iter (int): Iteraciones mínimas (requerido por PDF).
        
        Returns:
            Tuple (angles, message): (np.array de 3 ángulos, "Mensaje de estado")
                                     o (None, "Mensaje de error")
        """
        
        # 1. Verificar Límites del Espacio de Trabajo
        dist_sq = x_target**2 + y_target**2
        if dist_sq > self.max_reach**2:
            msg = "Error: El punto está fuera del alcance máximo."
            return None, msg

        target_pose = (x_target, y_target, phi_target)
        
        # 2. Definir la estimación inicial (q_k)
        if isinstance(initial_guess, str) and initial_guess == "random":
            # PDF: a. Valores Iniciales Aleatorios
            q_k = np.random.rand(3) # Rango [0, 1] rad
        elif isinstance(initial_guess, str) and initial_guess == "current":
            q_k = self.current_angles
        else:
            q_k = np.array(initial_guess)
        
        # 3. Bucle de Newton-Raphson
        for i in range(max_iter):
            # Calcular el vector de error F(q)
            F = self._calculate_F(q_k, target_pose)
            
            # Condición de paro (umbral de error + iteraciones mínimas)
            error = np.linalg.norm(F)
            if error < tolerance and i >= min_iter:
                q_k_normalized = np.arctan2(np.sin(q_k), np.cos(q_k))
                msg = f"Convergencia en {i} iteraciones."
                return q_k_normalized, msg

            # Calcular la Matriz Jacobiana J(q)
            J = self._calculate_jacobian(q_k)
            
            # Manejo de Singularidades (Det[J]=0)
            det_J = np.linalg.det(J)
            if abs(det_J) < 1e-8:
                msg = f"Error: Singularidad detectada (Det[J] ~ 0) en iter {i}."
                return None, msg # Fallamos si encontramos una singularidad

            # Resolver el sistema lineal: J * delta_q = -F
            delta_q = np.linalg.solve(J, -F)
            
            # Actualizar la estimación: q_k+1 = q_k + delta_q
            q_k = q_k + delta_q
            
        # Si el bucle termina, no hubo convergencia
        msg = f"Error: Newton-Raphson no convergió después de {max_iter} iteraciones."
        return None, msg


# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    
    # Definimos un robot RRR con longitudes 10, 8, y 5
    robot = PlanarManipulator(link_lengths=[10, 8, 5])
    
    # Establecer la posición inicial del robot en "Home"
    robot.set_current_angles(robot.get_home_angles())
    print(f"Posición Home: {np.rad2deg(robot.current_angles)}")
    
    # Definimos un punto objetivo
    # (x=15, y=5, orientacion=0 radianes)
    x_obj = 15.0
    y_obj = 5.0
    phi_obj = 0.0 # 0 radianes = 0 grados
    
    print("\n--- 1. Prueba de Cinemática Inversa (Numérica) ---")
    
    # Buscamos la solución cerca de la posición actual ("current")
    # Este es el modo por defecto, por lo que `initial_guess="current"` es opcional
    sol_num, msg = robot.inverse_kinematics(x_obj, y_obj, phi_obj)
    
    if sol_num is not None:
        print(f"Estado: {msg}")
        print(f"Ángulos encontrados: {np.rad2deg(sol_num)}")
        
        # Verificamos la posición final con DK
        joint_pos = robot.direct_kinematics(sol_num)
        end_effector_pos = joint_pos[-1]
        print(f"Posición alcanzada (DK): (x={end_effector_pos[0]:.4f}, y={end_effector_pos[1]:.4f})")
        
        # IMPORTANTE: Actualizar el estado del robot
        robot.set_current_angles(sol_num)
        print(f"Nuevo estado del robot: {np.rad2deg(robot.current_angles)}")

    else:
        print(f"Estado: {msg}")

    print("\n--- 2. Ejemplo de Punto Inalcanzable ---")
    # Punto fuera del alcance máximo (10+8+5 = 23)
    sol_num, msg = robot.inverse_kinematics(30.0, 0.0, 0.0)
    print(f"Estado: {msg}")
import numpy as np
from typing import Union

class PlanarRRRArm:
    """
    Gestiona la cinemática para un brazo robot RRR planar de 3-GDL.
    Las longitudes (l1, l2, l3) son para los tres eslabones.
    Todos los ángulos están en radianes para los cálculos.
    """
    def __init__(self, l1: float, l2: float, l3: float):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.link_lengths = np.array([l1, l2, l3])

    def forward_kinematics(self, thetas: list[float]) -> tuple[float, float]:
        """
        Calcula la posición (x, y) del efector final dados los ángulos.
        :param thetas: [theta1, theta2, theta3] en radianes.
        :return: (x, y) del efector final.
        """
        t1, t2, t3 = thetas
        x = (self.l1 * np.cos(t1) +
             self.l2 * np.cos(t1 + t2) +
             self.l3 * np.cos(t1 + t2 + t3))
        
        y = (self.l1 * np.sin(t1) +
             self.l2 * np.sin(t1 + t2) +
             self.l3 * np.sin(t1 + t2 + t3))
        
        return (x, y)

    def inverse_kinematics(self, x: float, y: float, phi_rad: float) -> Union[list[float], None]:
        """
        Calcula los ángulos [t1, t2, t3] (en radianes) para un
        punto (x, y) y una orientación del efector final (phi).
        
        :param x: Coordenada X del objetivo.
        :param y: Coordenada Y del objetivo.
        :param phi_rad: Orientación final deseada en radianes.
        :return: Lista de ángulos [t1, t2, t3] o None si es inalcanzable.
        """
        
        # 1. Calcular la posición de la muñeca (unión entre l2 y l3)
        # Retrocedemos l3 desde el efector final (x, y) con el ángulo phi.
        wx = x - self.l3 * np.cos(phi_rad)
        wy = y - self.l3 * np.sin(phi_rad)

        # 2. Ahora, resolvemos el problema 2-GDL para (wx, wy) con l1 y l2
        L1 = self.l1
        L2 = self.l2
        
        # Distancia al cuadrado desde el origen a la muñeca
        D_sq = wx**2 + wy**2
        
        # Verificar si el punto de la muñeca es alcanzable
        if D_sq > (L1 + L2)**2 or D_sq < (L1 - L2)**2:
            print(f"Error: Punto de muñeca ({wx:.2f}, {wy:.2f}) inalcanzable.")
            return None

        # Usar la ley de cosenos para encontrar theta2 (codo arriba)
        # (L1+L2)^2 < D_sq
        cos_theta2 = (D_sq - L1**2 - L2**2) / (2 * L1 * L2)
        # Asegurarse de que el valor esté en [-1, 1] para acos
        cos_theta2 = np.clip(cos_theta2, -1.0, 1.0) 
        
        theta2 = -np.arccos(cos_theta2) # Solución "codo arriba" (negativo por convención)
        
        # Encontrar theta1
        k1 = L1 + L2 * np.cos(theta2)
        k2 = L2 * np.sin(theta2)
        theta1 = np.arctan2(wy, wx) - np.arctan2(k2, k1)
        
        # 3. Encontrar theta3
        # phi = t1 + t2 + t3  =>  t3 = phi - t1 - t2
        theta3 = phi_rad - theta1 - theta2

        return [theta1, theta2, theta3]
# visualizer.py
import matplotlib.pyplot as plt
import numpy as np  # <--- 1. AÑADIR ESTA LÍNEA

class Visualizer:
    """
    Maneja la visualización del estado del robot usando Matplotlib.
    """

    def __init__(self, robot):
        """
        Inicializa el visualizador con una instancia del robot.
        """
        self.robot = robot
        # Añade un 10% de padding al alcance máximo para la gráfica
        self.plot_limit = self.robot.max_reach * 1.1 

    def plot_state(self, angles, target_pos=None):
        """
        Dibuja el estado actual del robot.

        :param angles: Los ángulos [t1, t2, t3] para dibujar.
        :param target_pos: Una tupla (x, y) opcional para dibujar el objetivo.
        """
        # Obtener las posiciones de las articulaciones
        joint_positions = self.robot.direct_kinematics(angles)
        
        # Separar coordenadas X e Y
        x_coords = [p[0] for p in joint_positions]
        y_coords = [p[1] for p in joint_positions]

        plt.figure(figsize=(8, 8))
        
        # Dibujar los eslabones del robot
        plt.plot(x_coords, y_coords, 'bo-', linewidth=3, markersize=10, label='Eslabones del Robot')
        
        # Marcar la base
        plt.plot(x_coords[0], y_coords[0], 'ks', markersize=15, label='Base (0,0)')
        
        # Marcar el efector final
        plt.plot(x_coords[-1], y_coords[-1], 'go', markersize=12, label='Efector Final')

        # Dibujar el objetivo si se proporciona
        if target_pos:
            plt.plot(target_pos[0], target_pos[1], 'rx', markersize=15, label='Objetivo')

        # Dibujar el círculo del espacio de trabajo
        workspace_circle = plt.Circle((0, 0), self.robot.max_reach, color='gray', 
                                      fill=False, linestyle='--', label='Alcance Máximo')
        plt.gca().add_patch(workspace_circle)

        
        # --- INICIO: CÓDIGO NUEVO PARA DIBUJAR PHI ---
        
        # 1. Obtener la posición del efector final
        ee_pos = joint_positions[-1]
        
        # 2. Calcular Phi (orientación absoluta)
        phi = np.sum(angles)
        
        # 3. Definir una longitud para la flecha (la mitad del último eslabón)
        arrow_len = self.robot.link_lengths[-1] * 0.5
        
        # 4. Calcular los componentes de la flecha
        dx = arrow_len * np.cos(phi)
        dy = arrow_len * np.sin(phi)
        
        # 5. Dibujar la flecha
        plt.arrow(ee_pos[0], ee_pos[1], dx, dy,
                  head_width=self.plot_limit * 0.02,  # Ancho de cabeza relativo al plot
                  head_length=self.plot_limit * 0.03, # Largo de cabeza relativo al plot
                  fc='m',  # 'm' es magenta
                  ec='m',
                  linewidth=2)
                  
        # 6. Añadir una etiqueta "ficticia" para la leyenda
        #    (plt.arrow no tiene 'label', así que usamos este truco)
        plt.plot([], [], color='m', marker='>', linestyle='None',
                 markersize=10, label='Orientación (phi)')
        
        # --- FIN: CÓDIGO NUEVO ---


        # Configuración de la gráfica
        plt.xlim(-self.plot_limit, self.plot_limit)
        plt.ylim(-self.plot_limit, self.plot_limit)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.legend() # <-- La leyenda ahora incluirá 'Orientación (phi)'
        plt.title('Simulador de Robot Planar de 3-GDL')
        plt.xlabel('Posición X')
        plt.ylabel('Posición Y')
        plt.show()
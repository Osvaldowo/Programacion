import math
import numpy as np # Necesario para los grados/radianes
from robot import PlanarManipulator
from visualizer import Visualizer # Asumo que tienes este archivo

def get_float_input(prompt):
    """ Función auxiliar para obtener una entrada numérica segura. """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

def main():
    # --- Configuración Inicial ---
    l1 = 5.0
    l2 = 4.0
    l3 = 3.0
    link_lengths = [l1, l2, l3]

    robot = PlanarManipulator(link_lengths)
    # Asumimos que visualizer.py existe y tiene una clase Visualizer
    # Si no lo tienes, puedes comentar las líneas de 'visualizer'
    visualizer = Visualizer(robot) 

    print(f"--- Simulador de Robot Planar 3-GDL ---")
    print(f"Eslabones: L1={l1}, L2={l2}, L3={l3}")
    print(f"Alcance máximo: {robot.max_reach}")
    print("---------------------------------------")
    
    # --- Mostrar el estado inicial (Home) ---
    print("Robot iniciando en posición 'Home'.")
    home_angles = robot.get_home_angles()
    home_pos = robot.direct_kinematics(home_angles)[-1]
    # Comenta la siguiente línea si no tienes visualizer.py
    visualizer.plot_state(home_angles, target_pos=home_pos)

    # --- Bucle Principal del Menú ---
    while True:
        print("\nElige un modo de operación:")
        print("  1. Cinemática Directa (Establecer nueva posición por ángulos)")
        print("  2. Cinemática Inversa (Calcular posición por objetivo)")
        print("  q. Salir")
        
        choice = input("Opción: ").strip()

        if choice == '1':
            # --- MODO: Cinemática Directa ---
            print("\n[Modo: Cinemática Directa]")
            t1_deg = get_float_input("  Introduce ángulo 1 (grados): ")
            t2_deg = get_float_input("  Introduce ángulo 2 (grados): ")
            t3_deg = get_float_input("  Introduce ángulo 3 (grados): ")

            angles_rad = np.radians([t1_deg, t2_deg, t3_deg])
            
            # 1. Actualizar el estado del robot
            robot.set_current_angles(angles_rad)
            
            # 2. Calcular y mostrar
            joint_positions = robot.direct_kinematics(angles_rad)
            ee_pos = joint_positions[-1] 
            print(f"\n  Posición del Efector Final: (x={ee_pos[0]:.3f}, y={ee_pos[1]:.3f})")
            # Comenta la siguiente línea si no tienes visualizer.py
            visualizer.plot_state(angles_rad)

        elif choice == '2':
            # --- MODO: Cinemática Inversa ---
            print("\n[Modo: Cinemática Inversa]")
            x = get_float_input("  Introduce coordenada X objetivo: ")
            y = get_float_input("  Introduce coordenada Y objetivo: ")
            phi_deg = get_float_input("  Introduce ángulo del efector final (grados): ")
            phi_rad = math.radians(phi_deg)

            # 1. Calcular la solución numérica.
            #    Por defecto, usará 'initial_guess="current"', que es
            #    lo que busca el movimiento "natural".
            solution, message = robot.inverse_kinematics(x, y, phi_rad)
            
            if solution is None:
                # Error: El punto no se pudo alcanzar
                print(f"\n  {message}") # Imprime el error (Fuera de alcance, Singularidad, etc.)
                
                # Mostramos el estado actual con el objetivo fallido
                # Comenta la siguiente línea si no tienes visualizer.py
                visualizer.plot_state(robot.current_angles, target_pos=(x, y))
            else:
                # Éxito: Se encontró una solución
                
                # 2. Actualizar el estado del robot a la solución elegida
                robot.set_current_angles(solution)
                
                angles_deg = np.degrees(solution)
                print(f"\n  Info: {message}") # Imprime el mensaje de éxito (ej. "Convergencia en 7 iteraciones")
                print(f"  Ángulos calculados (grados):")
                print(f"    Theta 1: {angles_deg[0]:.3f}°")
                print(f"    Theta 2: {angles_deg[1]:.3f}°")
                print(f"    Theta 3: {angles_deg[2]:.3f}°")
                
                # 3. Graficar el nuevo estado
                # Comenta la siguiente línea si no tienes visualizer.py
                visualizer.plot_state(solution, target_pos=(x, y))

        elif choice.lower() == 'q':
            print("Saliendo del simulador.")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
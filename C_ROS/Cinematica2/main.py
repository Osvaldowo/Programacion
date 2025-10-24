# main.py
import math
from robot import PlanarManipulator
from visualizer import Visualizer

def get_float_input(prompt):
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
    visualizer = Visualizer(robot)

    print(f"--- Simulador de Robot Planar 3-GDL ---")
    print(f"Eslabones: L1={l1}, L2={l2}, L3={l3}")
    print(f"Alcance máximo: {robot.max_reach}")
    print("---------------------------------------")
    
    # --- Mostrar el estado inicial (Home) ---
    print("Robot iniciando en posición 'Home'.")
    home_angles = robot.get_home_angles()
    home_pos = robot.direct_kinematics(home_angles)[-1]
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

            angles_rad = [math.radians(t1_deg), math.radians(t2_deg), math.radians(t3_deg)]
            
            # 1. Actualizar el estado del robot
            robot.set_current_angles(angles_rad)
            
            # 2. Calcular y mostrar
            joint_positions = robot.direct_kinematics(angles_rad)
            ee_pos = joint_positions[-1] 
            print(f"\n  Posición del Efector Final: (x={ee_pos[0]:.3f}, y={ee_pos[1]:.3f})")
            visualizer.plot_state(angles_rad)

        elif choice == '2':
            # --- MODO: Cinemática Inversa ---
            print("\n[Modo: Cinemática Inversa]")
            x = get_float_input("  Introduce coordenada X objetivo: ")
            y = get_float_input("  Introduce coordenada Y objetivo: ")
            print("  (El robot es redundante. Debes especificar la orientación final.)")
            phi_deg = get_float_input("  Introduce ángulo del efector final (grados): ")
            phi_rad = math.radians(phi_deg)

            # 1. Calcular ambas soluciones
            sol_up, sol_down = robot.inverse_kinematics(x, y, phi_rad)
            
            if sol_up is None:
                print(f"\n  Error: El punto (x={x}, y={y}) es inalcanzable con esa orientación.")
                # Mostramos el estado actual con el objetivo fallido
                visualizer.plot_state(robot.current_angles, target_pos=(x, y))
            else:
                # 2. Dejar que el robot elija la mejor solución
                chosen_solution, solution_name = robot.choose_best_solution(sol_up, sol_down)
                
                # 3. Actualizar el estado del robot a la solución elegida
                robot.set_current_angles(chosen_solution)
                
                angles_deg = [math.degrees(a) for a in chosen_solution]
                print(f"\n  Info: Solución '{solution_name}' elegida (movimiento mínimo).")
                print(f"  Ángulos calculados (grados):")
                print(f"    Theta 1: {angles_deg[0]:.3f}°")
                print(f"    Theta 2: {angles_deg[1]:.3f}°")
                print(f"    Theta 3: {angles_deg[2]:.3f}°")
                
                # 4. Graficar el nuevo estado
                visualizer.plot_state(chosen_solution, target_pos=(x, y))

        elif choice.lower() == 'q':
            print("Saliendo del simulador.")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
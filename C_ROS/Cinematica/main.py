import numpy as np
import time
from kinematics import PlanarRRRArm
from communication import ESP32Client

# --- CONFIGURACIÓN ---
# IP del ESP32 (obtenla del Monitor Serie de Arduino) 
ESP32_IP_ADDRESS = "192.168.1.100" 

# Longitudes de los eslabones (similar al PDF l2=5, l3=4)
# Añadimos l1.
L1 = 5.0
L2 = 5.0
L3 = 4.0

# --- INICIALIZACIÓN ---
arm = PlanarRRRArm(l1=L1, l2=L2, l3=L3)
client = ESP32Client(esp32_ip="10.87.10.3")

# --- EJECUCIÓN ---
def move_to_target(x: float, y: float, phi_deg: float):
    """
    Calcula y envía el comando para mover el brazo a un objetivo.
    """
    print(f"\n---> Moviendo a ({x}, {y}) con orientación {phi_deg}°")
    
    # 1. Calcular IK
    phi_rad = np.deg2rad(phi_deg)
    angles_rad = arm.inverse_kinematics(x, y, phi_rad)
    
    if angles_rad is None:
        print("Cálculo de IK falló. Misión abortada.")
        return

    # 2. Convertir ángulos a grados para los servos
    angles_deg = [np.rad2deg(a) for a in angles_rad]
    
    # mapear/restringir esto a [0, 180] para servos
    
    print(f"Ángulos (RAD): {angles_rad}")
    print(f"Ángulos (DEG): {angles_deg}")

    # 3. Verificar con FK (opcional)
    fk_pos = arm.forward_kinematics(angles_rad)
    print(f"Verificación FK: {fk_pos} (Debería ser cercano a {x, y})")

    # 4. Enviar a ESP32
    client.send_angles(angles_deg)

if __name__ == "__main__":
    # Prueba 1: Mover a una posición
    move_to_target(x=8.0, y=4.0, phi_deg=0)
    time.sleep(3) # Esperar a que los servos se muevan
    
    # Prueba 2: Mover a otra posición
    move_to_target(x=5.0, y=7.0, phi_deg=45)
    time.sleep(3)
import requests

class ESP32Client:  # <- CORRECCIÓN 1: Así se define la clase
    """
    Maneja la comunicación HTTP con el servidor del ESP32.
    """
    def __init__(self, esp32_ip: str):
        # La IP debe ser la que el ESP32 imprime en su monitor serie
        self.base_url = f"http://{esp32_ip}"
        print(f"Cliente inicializado para ESP32 en: {self.base_url}")

    def send_angles(self, angles_deg: list[float]) -> bool:
        """
        Envía los ángulos (en grados) al endpoint /set_angles del ESP32.
        :param angles_deg: Lista de ángulos [t1, t2, t3] en grados.
        :return: True si fue exitoso, False si falló.
        """
        t1, t2, t3 = angles_deg
        endpoint = f"{self.base_url}/set_angles"
        params = {
            "t1": f"{t1:.2f}",
            "t2": f"{t2:.2f}",
            "t3": f"{t3:.2f}"
        }

        try:
            # TimeConstrained[... 10 ...] del PDF es análogo al 'timeout'
            response = requests.get(endpoint, params=params, timeout=5)
            
            if response.status_code == 200 and response.text == "OK":
                print(f"Ángulos enviados: {params}, Respuesta: {response.text}")
                return True
            else:
                print(f"Error del servidor ESP32: {response.status_code} - {response.text}")
                return False
        
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
            return False
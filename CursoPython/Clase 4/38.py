# =================================================
# ============ Ejercicio 38 ========================
# =================================================
# Ejemplo con POO

from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass
    
class Paypal(MetodoPago):
    def __init__(self, correo):
        self.correo = correo

    def pagar(self, monto):
        print(f"Pagando {monto} usando PayPal con el correo {self.correo}.")

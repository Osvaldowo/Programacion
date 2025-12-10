# =========================================
# =========== Herencia ====================
# =========================================
# En este ejemplo, creamos una clase base 
# 'Vehiculo' y una clase derivada 'Motocicleta'
# que hereda de 'Vehiculo'. La clase derivada
# puede acceder a los métodos y atributos de la clase base.

class Vehiculo: 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} ha arrancado.")
        
class Motocicleta(Vehiculo):

    def hacer_caballito(self):
        print(f"La motocicleta {self.marca} {self.modelo} está haciendo un caballito!")
        
mi_moto = Motocicleta("Yamaha", "MT-07")
mi_moto.arrancar()
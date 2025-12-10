# Atributos

class Coche: 
    def __init__(self):
        print("Ensamblando auto")
        
        self.marca = "Patito"
        self.color = "chido"
        self.modelo = "Chevy pop"
        self.encendido = False
        
    def arrancar (self):
        self.encendido = True
        
mi_coche = Coche()

print(f"\nMi coche es de color: {mi_coche.color}")
print(f"\nEstado de mi auto: {mi_coche.encendido}")


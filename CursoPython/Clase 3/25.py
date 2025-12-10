# Constructor que pide parametros

class Coche: 
    def __init__(self, marca_input, color_input):
        print("Ensamblando auto")
        
        self.marca = marca_input
        self.color = color_input
        self.modelo = "Chevy pop"
        self.encendido = False
        
    def arrancar (self):
        self.encendido = True
        
    def tocar_claxon(self):
        print(f"El {self.marca} {self.modelo} hace pi pi pi")
        
mi_coche = Coche("Patito","Cabron")

print(f"\nMi coche es de color: {mi_coche.color}")
print(f"\nEstado de mi auto: {mi_coche.encendido}")

mi_coche.tocar_claxon()
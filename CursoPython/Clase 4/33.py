# =========================================
# =========== Polimorfismo ================
# =========================================
# El polimorfismo es un concepto de la programación 
# orientada a objetos que permite que diferentes clases 
# puedan ser tratadas de la misma manera a través de una interfaz común. 
# En Python, esto se logra mediante la definición de 
# métodos con el mismo nombre en diferentes clases.

class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")
        
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra: ¡Guau Guau!")
        
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla: ¡Miau Miau!")
        
zoo = [Perro(), Gato(), Animal()]
for animal in zoo:
    animal.hacer_sonido()
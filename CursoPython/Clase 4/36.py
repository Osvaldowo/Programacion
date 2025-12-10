# =======================================
# ============== Métodos ================
# =======================================
# Los métodos son funciones definidas dentro de una clase y 
# se utilizan para definir el comportamiento de los objetos creados a partir de esa clase.
# Los métodos pueden acceder y modificar los atributos del objeto.
# Los métodos especiales, como __init__, __str__, etc., tienen significados específicos en Python.
# Usa cls en lugar de self para referirte a la clase en métodos de clase.

from datetime import date


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    @classmethod    
    def desde_nacimiento(cls, nombre, año_nacimiento):
        
        edad_calculada = date.today().year - año_nacimiento
        return cls(nombre, edad_calculada)
    
p1 = Persona("Oswiwi", 24)

p2 = Persona.desde_nacimiento("Ana", 1990)

p2.presentarse()
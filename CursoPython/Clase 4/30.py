# ====================================
# ========= Setter n' Getter =========
# ====================================
# Los getters y setters son métodos especiales 
# que permiten controlar el acceso a los atributos de una clase.
# En Python, se utilizan decoradores @property para definir getters
# y el decorador @<nombre_del_getter>.setter para definir setters.

class Usuario:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo "protegido"
        self._edad = edad      # Atributo "protegido"

    # Getter para el nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para el nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Getter para la edad
    @property
    def edad(self):
        return self._edad

    # Setter para la edad
    @edad.setter
    def edad(self, nueva_edad):
        print("Intentando actualizar la edad...")
        if nueva_edad > 0:
            self._edad = nueva_edad
            print("Edad actualizada correctamente")
        else:
            print("La edad no puede ser negativa")
        
usr = Usuario("Oswiwi", 24)

print(f"Nombre: {usr.nombre}")
print(f"Edad: {usr.edad}")

usr.edad = -5
usr.edad = 25
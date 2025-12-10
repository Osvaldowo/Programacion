# =========================================
# =========== Herencia ====================
# =========================================
# Ejemplo 2: Herencia con método sobrescrito y uso de super()
# super() permite llamar al método de la clase base

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")
        
class Gerente(Empleado):
    def __init__(self, nombre, salario, departameno):
        super().__init__(nombre, salario)
        
        self.departameno = departameno

    def trabajar(self):
        print(f"Salario: {self.nombre} está gestionando el departamento de {self.departameno}.")
        
g = Gerente("Oswiwi", 5000, "Ventas")
g.trabajar()
print(f"Salario del gerente: {g.salario}")
print(f"Departamento del gerente: {g.departameno}")
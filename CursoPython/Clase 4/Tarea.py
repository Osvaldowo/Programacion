class Esclavo:
    def __init__(self, id, nombre, puesto, salario):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto 
        self.salario = salario 
        
    def __str__(self):
        return f"[ID: {self.id}. {self.nombre} | {self.puesto} | Salario: {self.salario}]"
    
    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        print(f"Salario aumentado exitosamente!! \nNuevo salario: {self.salario}")
        
def registrar_empleado(lista):
    print("====== Nuevo Empleado ======")
    n_nombre = input("Como se llama el nuevo empleado? ")
    n_puesto = input("Que puesto desarrollara? ")
    try:
        n_salario = int(input("Cual sera su salario? "))
        n_id = len(lista) + 1
        nuevo_empleado = Esclavo(n_id, n_nombre, n_puesto, n_salario)
        lista.append(nuevo_empleado)
    except ValueError:
        print("Salario invalido. Intenta con numeros.")

def mostrar_nomina(lista):
    print("====== Nomina de Empleados ======")
    for empleado in lista:
        print(empleado)
        
def buscar_empleado(lista, id):
    for empleado in lista:
        if empleado.id == id:
            return empleado
    return None
        
def main():
    empleados = []
    while True:
        print("\n1. Registrar nuevo empleado")
        print("2. Mostrar nomina de empleados")
        print("3. Aumentar salario de un empleado")
        print("4. Buscar empleado por ID")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_empleado(empleados)
        elif opcion == "2":
            mostrar_nomina(empleados)
        elif opcion == "3":
            porcentaje_aumento = float(input("Ingrese el porcentaje de aumento: "))
            id_buscar = int(input("Ingrese el ID del empleado para aumentar su salario: "))
            empleado = buscar_empleado(empleados, id_buscar)
            if empleado:
                empleado.aumentar_salario(porcentaje_aumento)
            else:
                print("Empleado no encontrado.")
        elif opcion == "4":
            id_buscar = int(input("Ingrese el ID del empleado a buscar: "))
            empleado = buscar_empleado(empleados, id_buscar)
            if empleado:
                print(empleado)
            else:
                print("Empleado no encontrado.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            
if __name__ == "__main__":
    main()
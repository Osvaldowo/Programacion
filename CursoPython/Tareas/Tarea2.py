# ==================================================
# ==================================================
# ========= Tarea 2 - Curso de Python ==============
# ==================================================
# ==================================================

# Autor: [Osvaldo Flores Oropeza]
# Fecha: [19 de Noviembre de 2025]

class CuentaBancaria: 
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial
        
    def __str__(self):
        return f"Titular= {self._titular}, Saldo= {self._saldo}"
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @titular.setter
    def titular(self, n_titular):
        self._titular = n_titular
        
    @saldo.setter
    def saldo(self, n_saldo):
        try:
            nn_saldo = float(n_saldo)
        except (TypeError, ValueError):
            raise TypeError("El saldo debe ser un valor numérico.")
        if nn_saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = nn_saldo
        print(f"Saldo actualizado a: {self._saldo}")
    
    def depositar(self, cantidad):
        try:
            n_cantidad = float(cantidad)
        except (Exception):
            raise TypeError("La cantidad debe ser un valor numérico.")
        if n_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativo.")
        self.saldo += n_cantidad
        
    def retirar(self, cantidad):
        try:
            n_cantidad = float(cantidad)
        except (Exception):
            raise TypeError("La cantidad debe ser un valor numérico.")
        if n_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativo.")
        if n_cantidad > self._saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        self.saldo -= n_cantidad

titular = input("Ingrese el nombre del titular de la cuenta: ")
cuenta = CuentaBancaria(titular)

def menu():
    print(f"=== Menú de Cuenta Bancaria de {titular} ===")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar información de la cuenta")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    return opcion

while True:
    opcion = menu()
    if opcion == "1":
        print(f"Saldo actual: {cuenta.saldo}")
    elif opcion == "2":
        cantidad = input("Ingrese la cantidad a depositar: ")
        try:
            cuenta.depositar(cantidad)
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
    elif opcion == "3":
        cantidad = input("Ingrese la cantidad a retirar: ")
        try:
            cuenta.retirar(cantidad)
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
    elif opcion == "4":
        print(cuenta)
    elif opcion == "5":
        print("Saliendo del programa. ¡Gracias por usar el sistema bancario!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


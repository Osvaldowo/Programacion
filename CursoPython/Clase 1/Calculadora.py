print("Calculadora")
print("1. Suma")
print("1. Resta")
print("1. División")
print("1. Multiplicación")
print("1. Salir")

opcion = input("Selecciona una opción:")

if opcion == '1':
    num1 = int ( input("Dame un número: "))
    num2 = int ( input("Dame un número: "))
    
    suma = num1 + num2
    
    print(f"La suma de {num1} + {num2} es {suma}")
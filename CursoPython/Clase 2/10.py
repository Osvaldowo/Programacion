import numpy as np

def Suma(a, b):
    return a + b

def SumaNP(a, b):
    return np.add(a, b)

def Resta(a, b):
    return a - b

def RestaNP(a, b):
    return np.subtract(a, b)    

def Multiplicacion(a, b):
    return a * b

def MultiplicacionNP(a, b):
    return np.multiply(a, b)

def Division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero"
    
def DivisionNP(a, b):
    if b == 0:
        return "Error: Division por cero"
    else: 
        return np.divide(a, b)
    
while True:
    print("Seleccione la operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    eleccion = input("Ingrese su opcion (1/2/3/4/5): ")
    
    if eleccion == '5':
        print("Saliendo del programa.")
        break
    
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    if eleccion == '1':
        print(f"{num1} + {num2} = {Suma(num1, num2)}")
        print(f"Usando NumPy: {num1} + {num2} = {SumaNP(num1, num2)}")
    elif eleccion == '2':
        print(f"{num1} - {num2} = {Resta(num1, num2)}")
        print(f"Usando NumPy: {num1} - {num2} = {RestaNP(num1, num2)}")
    elif eleccion == '3':
        print(f"{num1} * {num2} = {Multiplicacion(num1, num2)}")
        print(f"Usando NumPy: {num1} * {num2} = {MultiplicacionNP(num1, num2)}")
    elif eleccion == '4':
        print(f"{num1} / {num2} = {Division(num1, num2)}")
        print(f"Usando NumPy: {num1} / {num2} = {DivisionNP(num1, num2)}")
    else:
        print("Opcion invalida. Por favor intente de nuevo.")
        
    input("\n")
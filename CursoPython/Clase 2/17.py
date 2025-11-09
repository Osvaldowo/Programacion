import numpy as np

#Funciones sin parametros

def saludar():
    print("Hola, esta es mi primera funcion!")
    
print("Llamando a la funcion saludar:")

saludar()

#Funciones con parametros


def saludar_a_alguien(nombre_usuario):
    print(f"Hola, {nombre_usuario}! Bienvenido a mi programa.")
    
saludar_a_alguien("Oswiwi")
saludar_a_alguien(1)

#Funciones con valor de retorno

def sumar_numeros(num1, num2):
    resultado = num1 + num2
    return resultado

resultado_suma = sumar_numeros(5, 10)
print(f"El resultado de la suma es: {resultado_suma}")

def division(dividendo, divisor):
    resultado = np.divide(dividendo, divisor)
    return resultado

resultado_division = division(10, 2)
print(f"El resultado de la division es: {resultado_division}")
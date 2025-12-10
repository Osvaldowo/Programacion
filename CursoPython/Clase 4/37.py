# =================================================
# ============== Métodos Estáticos ================
# =================================================
# En Python, los métodos estáticos son aquellos que 
# pertenecen a una clase en lugar de a una instancia específica de la clase.
# Se definen utilizando el decorador @staticmethod.
# Los métodos estáticos no pueden acceder a los atributos o métodos de instancia


class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Error: División por cero."
        return a / b
    @staticmethod
    def info():
        print("Esta es una calculadora básica que puede sumar, restar, multiplicar y dividir.")
    
print(f"Suma: {Calculadora.sumar(5, 3)}")
Calculadora.info()

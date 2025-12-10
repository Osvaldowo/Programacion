# =========================================================
# ================ Try - Except - =========================
# =========================================================

try: 
    
    val1 = int(input("Ingrese el dividendo: "))
    val2 = int(input("Ingrese el divisor: "))
    
    res = val1 / val2
    print(f"El resultado de la división es: {res}")
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debe ingresar números válidos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
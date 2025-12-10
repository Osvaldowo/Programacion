# =========================================================
# ================ Try - Except - =========================
# =========================================================


try: 
    numero_texto = input("Ingrese un número: ")
    numero = int(numero_texto)
    print(f"El número ingresado es: {numero + 10}")
    
except ValueError:
    print(f"ERROR: '{numero_texto}' no es un número válido.")
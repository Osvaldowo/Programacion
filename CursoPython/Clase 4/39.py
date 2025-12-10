# =========================================================
# ================ Try - Except - =========================
# =========================================================
# En este ejemplo, se intenta dividir 10 por un número ingresado por el usuario.
# Si el usuario ingresa un valor no numérico o cero, se captura la excepción


try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print(f"El resultado de la división es: {resultado}")
    
except:
    print("Error: Debe ingresar un número válido.")

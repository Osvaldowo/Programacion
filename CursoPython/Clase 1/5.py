# Entrada de datos

nombre_usuario = input("Por favor, escribe tu nombre: ")

año_nacimiento_str = int (input("Ahora, ingresa escribe tu año de nacimiento:"))

año_actual = 2025
edad_calculada = año_actual - año_nacimiento_str

print(f"Hola, {nombre_usuario}. Si estamos en {año_actual}, tu edad es de {edad_calculada}")


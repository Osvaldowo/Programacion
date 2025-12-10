# =========================
# Manejo de Errores
# =========================

lista_frutas = ["manzana", "banana", "cereza"]

try: 
    indice = int(input("Ingrese un índice para acceder a la lista de frutas (0-2): "))
    print(f"La fruta en el índice {indice} es: {lista_frutas[indice]}")
    
except Exception as e: 
    print("\n¡Ocurrió un error al intentar acceder a la lista!")
    print (f"Mensaje tecnico del error: {e}")
    print("Tipo de error:", type(e).__name__)
    
try: 
    
    edad_str = input("\nIngrese su edad: ")
    edad = int(edad_str)
    
except ValueError as ve:
    print("\n¡Error: La edad debe ser un número entero!")
    print(f"Mensaje tecnico del error: {ve}")
    print("Tipo de error:", type(ve).__name__)
    
# =========================
# Manejo de Errores - Finally
# =========================   

try: 
    print("1. Abriendo conexión a base de datos...")
    resultado = 10 / 0  # Esto generará una excepción   
    print("2. Ejecutando consulta en la base de datos...")
except ZeroDivisionError as zde:
    print("\n¡Error: División por cero no permitida!")
    print(f"Mensaje tecnico del error: {zde}")
    print("Tipo de error:", type(zde).__name__)
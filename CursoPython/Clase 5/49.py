# ==============================================
# Lectura y escritura de archivos en Python
# ==============================================

print("Abriendo el archivo 'mi_diario.txt' para lectura...")

try: 
    with open("mi_diario.txt", 'r', encoding='utf-8') as archivo:
        print("Leyendo el contenido del archivo...\n")
        contenido = archivo.read()
        
        print("-- Inicio de la lectura línea por línea --")
        print(contenido)
        
except FileNotFoundError:
    print("Error: El archivo 'mi_diario.txt' no se encontró.")
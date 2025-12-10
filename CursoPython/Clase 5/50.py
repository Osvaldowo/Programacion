# ===================================
# Modo de uso Agregar ('a') en archivos
# ===================================   

nombre_archivo = "mi_diario.txt"
print(f"Abriendo el archivo '{nombre_archivo}' en modo agregar ('a')...")
# Abrir el archivo en modo agregar ('a')
with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
    print("Agregando nuevas líneas al archivo...")
    archivo.write("Hoy también aprendí sobre el modo agregar en archivos.\n")
    archivo.write("¡Ahora puedo añadir contenido sin borrar lo anterior!\n")
    print("Nuevas líneas agregadas exitosamente.")
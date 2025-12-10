# =====================================
# Manejo de archivos en Python
# =====================================

nombre_archivo = "mi_diario.txt"

print(f"Abriendo el archivo '{nombre_archivo}'...")

# Abrir el archivo en modo escritura ('w')
with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    print("Escribiendo en el archivo...")
    archivo.write("Querido diario,\n")
    archivo.write("Hoy aprendí a manejar archivos en Python.\n")
    archivo.write("¡Es muy interesante!\n")
    print("Escritura completada.")
    
print(f"Archivo escrito exitosamente")

# Sin cerrar el archivo

with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write("Esta es una nueva línea en el archivo.\n")
    archivo.write("Sobrescribiendo el contenido anterior.\n")
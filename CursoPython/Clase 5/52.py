# ======================================
# Archivos a lista
# ======================================

nombre = "lista_de_compras.txt"

compras = ["manzanas", "plátanos","naranjas","pan",]

print(f"Escribiendo la lista de compras en el archivo '{nombre}'...")
with open(nombre, 'w', encoding='utf-8') as archivo:
    for item in compras:
        archivo.write(f"{item}\n") 
print("Lista de compras escrita exitosamente.") 

lista_leida = []
print(f"Leyendo la lista de compras desde el archivo '{nombre}'...")
with open(nombre, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        lista_leida.append(linea.strip())
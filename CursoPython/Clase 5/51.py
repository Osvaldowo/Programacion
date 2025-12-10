# ===============================
# Procesar (p) para archivos
# ===============================

print("Analizando el archivo linea por línea con procesamiento personalizado...")

with open("mi_diario.txt", 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        linea_procesada = linea.strip().upper()
        print(f"Línea procesada: {linea_procesada}")
print("Procesamiento completado.")  
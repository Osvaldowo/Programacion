"""Diccionarios
"""

# Definicion de un diccionario
estudiante = {
    "estudiante":"Oswiwi",
    "edad":24,
    "curso":"Python",
    "Esta_Activo":True
}

print(f"Nombre del estudiante: {estudiante['estudiante']}")
print(f"Edad del estudiante: {estudiante['edad']}")
print(f"Curso del estudiante: {estudiante['curso']}")
print(f"¿El estudiante esta activo?: {estudiante['Esta_Activo']}")

# Agregar un nuevo par clave-valor
estudiante["promedio"] = 95.5
print(f"Promedio del estudiante: {estudiante['promedio']}")

# Recorrer el diccionario

print("\n--- Recorrido del Diccionario ---")
for clave, valor in estudiante.items():
    print(f"    -Clave: {clave}, Valor: {valor}")
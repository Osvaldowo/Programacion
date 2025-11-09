# --- Bienvenido al Analizador de Calificaciones ---
print("--- Bienvenido al Analizador de Calificaciones ---")
# 1. Pedimos el nombre del estudiante (str)
nombre_estudiante = input("Introduce el nombre del estudiante: ")
# 2. Creamos una lista fija de calificaciones (int)
calificaciones = []

numero_materias = input("Introduce el numero de materias que quieres registrar: ")

for i in range(int(numero_materias)):
    calificacion = int((input(f"Introduce la calificacion de la materia {i + 1}: ")))
    calificaciones.append(calificacion)

calificacion_aprobatoria = 6
# 3. Inicializamos variables para los calculos
total_calificaciones = 0
materias_aprobadas = 0
materias_reprobadas = 0
# 4. Usamos un bucle ’for’ para recorrer la lista
for calificacion in calificaciones:
    # Sumamos la calificacion actual al total
    total_calificaciones = total_calificaciones + calificacion
    # 5. Verificamos si la calificacion es aprobatoria
    if calificacion >= calificacion_aprobatoria:
        materias_aprobadas = materias_aprobadas + 1
    else:
        materias_reprobadas = materias_reprobadas + 1
# 6. Calculamos el promedio
# Usamos len() para saber cuantos elementos hay
promedio = total_calificaciones / len(calificaciones)
# 7. Mostramos el resumen final usando f-strings
print("\n--- Resumen del Estudiante ---")
print(f"Estudiante: {nombre_estudiante}")
print(f"Calificaciones: {calificaciones}")
print(f"Promedio Final: {promedio:.2f}")
print(f"Materias Aprobadas: {materias_aprobadas}")
print(f"Materias Reprobadas: {materias_reprobadas}")
if promedio >= calificacion_aprobatoria:
    print("¡Felicidades! El estudiante ha aprobado.")
else:
    print("El estudiante necesita mejorar.")
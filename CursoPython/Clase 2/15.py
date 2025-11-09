"""
Tuplas
"""

coordenadas_gps = (19.432608, -99.133209)

print(f"Latitud: {coordenadas_gps[0]}")
print(f"Longitus: {coordenadas_gps[1]}")

latitud, longitud = coordenadas_gps
print(f"Latitud desempaquetada: {latitud}")

coordenadas_gps[0] = 20.0  # Esto generará un error porque las tuplas son inmutables

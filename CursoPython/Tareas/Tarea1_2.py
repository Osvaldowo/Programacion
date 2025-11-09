import os
# ======== Lista De Compras ========

print("Hola, esta es tu lista de compras!")

nombres = []
cantidad = []
precios = []
articulos = [nombres, cantidad, precios]

total_de_articulos = input("Cuantos archivos quieres agregar a tu lista? \n")

for i in range(int(total_de_articulos)):
    nombre_articulo = input("Cual es el nombre del articulo? \n")
    nombres.append(nombre_articulo)
    cantidad_articulo = int(input("Cuantas piezas quieres comprar? \n"))
    cantidad.append(cantidad_articulo)
    precio_articulo = float(input("Cuanto cuesta el producto? \n"))
    precios.append(precio_articulo)
    
    
total_compra = 0

for i in range(int(total_de_articulos)):
    total_compra = (articulos[1][i] * articulos[2][i]) + total_compra

os.system('cls')
print("==== !!! Te presento tu lista completa !!! ===")

for i in range(int(total_de_articulos)):
    print(f"\n{i+1}. {articulos[0][i]}, {articulos[1][i]} piezas a {articulos[2][i]}")
    
print(f"\nTotal de compra: {total_compra}")
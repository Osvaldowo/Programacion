print("Este bucle se repetira hasta que escribas 'salir'.")

while True:
    
    texto= input("Escribe algo (o 'salir' para terminar):")
    
    if texto.lower() == 'salir':
        print("Has decidido salir del bucle.")
        break
    
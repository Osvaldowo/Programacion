import random

def bubble_sort(lista_desordenada):
    # Hacemos una copia para no destruir la original
    lista = lista_desordenada.copy()
    n = len(lista) # Total de elementos
    # Bucle externo (i)
    for i in range(n):
        # Bucle interno (j)
        for j in range(0, n - i - 1):
            # La comparacion clave:
            if lista[j] > lista[j + 1]:
                # El intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista # Devolvemos la lista ordenada

def main():
# El bucle ’while True’ se repite para siempre
    while True:
        print("\n--- ORDENADOR DE ARREGLOS (BURBUJA) ---")
        print("1. Ingresar arreglo manualmente")
        print("2. Generar arreglo aleatorio")
        print("3. Salir")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            print("...Aqui ira la funcion manual...")
            modo_manual()
        elif opcion == "2":
            print("...Aqui ira la funcion aleatoria...")
            modo_aleatorio()
        elif opcion == "3":
            print("¡Adios!")
            break # ’break’ rompe el bucle
        else:
            print("Opcion no valida. Intenta de nuevo.")
            
def modo_manual():
    print("\n--- Modo Manual ---")
    mi_lista = [] # Lista vacia
    try:
        total_numeros = int(input("Cuantos numeros vas a ingresar?: "))
        for i in range(total_numeros):
            num = int(input(f"Ingresa el numero {i + 1}: "))
            mi_lista.append(num)
            print(f"\nTu lista original: {mi_lista}")
            # --- AQUI USAMOS NUESTRA HERRAMIENTA ---
            lista_ordenada = bubble_sort(mi_lista)
            print(f"Tu lista ordenada: {lista_ordenada}")
    except ValueError:
        print("Error: Debes ingresar solo numeros.")
        
def modo_aleatorio():
    print("\n--- Modo Aleatorio ---")
    try:
        total_numeros = int(input("Cuantos numeros quieres generar?: "))
        minimo = int(input("Valor minimo del rango: "))
        maximo = int(input("Valor maximo del rango: "))
        mi_lista = []
        for _ in range(total_numeros):
            num_aleatorio = random.randint(minimo, maximo)
            mi_lista.append(num_aleatorio)
            print(f"\nLista generada (desordenada): {mi_lista}")
            # --- AQUI USAMOS NUESTRA HERRAMIENTA ---
            lista_ordenada = bubble_sort(mi_lista)
            print(f"Lista ordenada: {lista_ordenada}")
    except ValueError:
        print("Error: Debes ingresar solo numeros.")
        
main()

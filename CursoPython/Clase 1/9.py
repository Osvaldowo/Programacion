# Bucles

numeros = [28, 5, -8, 25, 0, 100]

print("Analizando la lista de números...")

for numero in numeros:
    
    if numero > 10:
        print(f"El número {numero} es mayor que 10.")
        
    elif numero == 0:
        print(f"El número es {numero}")
        
    else: 
        print(f"El número {numero} es menor a 10")
        
print("\nAnálisis completado")
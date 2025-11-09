import random as r

print("He pensado un numero entre 1 y 20. Puedes adivinar cual es?")

numero_secreto = r.randint(1,20)

intento = 0

while intento != numero_secreto:
    
    intento = int(input("Introduce tu numero:"))
    
    if intento < numero_secreto:
        print("Numero muy pequeño D:")
    elif intento > numero_secreto:
        print("Numero muy grande :D")
        
print("Felicidades! Has adivinado el numero secreto :D")
        
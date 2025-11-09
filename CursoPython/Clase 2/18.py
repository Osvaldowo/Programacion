#Variables Globales

variable_global = "Soy una variable global"

def funcion_ejemplo():
    
    variable_local = "Soy una variable local"
    
    global variable_global
    variable_global = "Me modificaron noooo"
    
    print(f"Dentro de la funcion, puedo ver la variable: {variable_local}")
    print(f"Dentro de la funcion, tambien puedo ver la variable global: {variable_global}")
    
print("Llamando a la funcion:")
funcion_ejemplo()

print(f"Fuera de la funcion, la variable global es: {variable_global}")


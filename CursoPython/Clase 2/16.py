"""
Conjuntos (set)
"""

lista_invitados = ["Ana", "Luis", "Carlos", "Marta", "Ana", "Luis"]
print(f"Lista original de invitados: {lista_invitados}")

invitados_unicos = set(lista_invitados)
print(f"Lista de invitados unicos (set): {invitados_unicos}")

invitados_unicos.add("Sofia")
invitados_unicos.add("Carlos")  # No se agregara porque ya existe
print(f"Lista de invitados unicos despues de agregar nuevos invitados: {invitados_unicos}")
"""Class List"""

to_do = ["Ir al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]

print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers), numbers)

mix = ["uno", 2, 3.14, True, [1, 2, 3]]

print(mix)
print(len(mix))

print(f"Elemento 1: {mix[0]}")
print(f"Elemento 2: {mix[0]}")
print(f"Elemento 3: {mix[0]}")
print(f"Elemento Fin: {mix[-1]}")

# Slicing [elemento:elemento]
print(mix[:2]) # mix[0:2] -> Posicion 0 hasta 1, 2 se excluye.
print(mix[2:]) # mix[2:0] --> Posicion 2 hasta el final.

# Metodos

# append -> Agrega un elemento al final.
mix.append(False)
print(mix)

mix.append(["a", "b"])
print(mix)

# insert --> Agrega un elemento en la posición X.
mix.insert(1, ["a", "b"])
print(mix)

# index --> Consultar elemento, retorna la posición.
# Si el elemento se encuentra dos veces, retorna el primero que encuentre.
print(mix.index(["a", "b"]))

print('\n')

# Elemento mayor y menor de una lista
numbers = [1, 2, 3, 4, 100, 3]

print(numbers)
print("Mayor:", max(numbers))
print("Menor:", min(numbers))

# Eliminar elemento
del numbers[0]
print(numbers)

del numbers[:2]
print(numbers)

# Eliminar toda la lista
del numbers
#print(numbers) # Error ya que no existe la lista.
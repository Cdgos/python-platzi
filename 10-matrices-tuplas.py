matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matriz)

# Primera Posicion
print(matriz[0][0])

"""
Una tupla en Python es una estructura de datos inmutable que 
permite almacenar un conjunto de elementos, muy similar a una 
lista, pero con la diferencia principal de que una vez creada 
no se puede modificar (no se pueden añadir, eliminar ni cambiar 
elementos).
"""

# Tuplas
numbers = (1, 2, 3, 4, 5)
print(type(numbers), numbers)

# Si intentamos modificarla: ERROR
# numbers[0] = 'uno'
# print(numbers)
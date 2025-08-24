"""
📘 Copia de listas en Python: referencia vs copia independiente

En Python, cuando copiamos listas, debemos tener en cuenta que no siempre se 
crea una nueva lista. A veces, simplemente estamos copiando la *referencia* 
(la dirección en memoria) y no los valores como tal.

➡ Caso 1: Copia por referencia
Si hacemos `b = a`, lo que ocurre es que `b` NO es una lista nueva, sino 
otra variable que apunta al mismo espacio en memoria que `a`. 

Esto significa que cualquier cambio en `a` también se verá reflejado en `b`, 
y viceversa.

➡ Caso 2: Copia independiente (shallow copy)
Si queremos una copia que NO comparta memoria con la lista original, 
podemos usar técnicas como:
    - Slicing: `b = a[:]`
    - Función `list()`: `b = list(a)`
    - Módulo `copy`: `import copy; b = copy.copy(a)`

De esta forma, `b` contendrá los mismos elementos, pero será una lista 
independiente.
"""

# ------------------------------
# EJEMPLO: Copia por referencia
# ------------------------------
a = [1, 2, 3, 4, 5]
b = a   # b apunta al mismo espacio en memoria que a

print("Antes de modificar:")
print("a:", a)
print("b:", b)

print("\n")

# Modificamos la lista 'a'
del a[0]   # eliminamos el primer elemento

# Como 'b' apunta al mismo lugar en memoria, también se ve afectada
print("Después de eliminar el primer elemento de 'a':")
print("a:", a)
print("b:", b)

# Verificación del mismo espacio en memoria:
print("id(a):", id(a))
print("id(b):", id(b))

print("\n")

# ------------------------------
# SLICING
# ------------------------------

c = a[:]

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c)) # Id diferente que a y b.

a.append(6) # Lo añade en a y b, en c ya no tenemos el problema.

print("a:", a)
print("b:", b)
print("c:", c)
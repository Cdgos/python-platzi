full_name = """Johan
Sebastian
"""
print(type(full_name))
print(full_name)

name = "JOHAN Sebastian"
last_name = "  Casadiegos GOMEZ "

print(name)
print(last_name)

print('\n')

print(name[0])
print(name[1])
print(name[2])

print(name[-1])  # Último
print(name[-2])  # Penúltimo

print('\n')

print(name * 5)

# Concatenacion
print(name + " " + last_name)

# Longitud
print(len(name))

# Metodo minusculas
print(name.lower())

# Metodo mayusculas
print(name.upper())

# Eliminar espacios al inicio y fin
print(last_name.strip())

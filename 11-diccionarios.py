# Diccionarios {clave:valor}

persona = {
    "nombre": "Sebastian",
    "apellido": "Casadiegos",
    "edad": 24,
    "altura": 1.85,
    "empleado": True,
}

print(persona)

# Obtener valor, le pasamos clave
print(persona["nombre"])

# Eliminar
del persona["empleado"]
print(persona)

# Obtener las claves
claves = persona.keys()
print(claves)
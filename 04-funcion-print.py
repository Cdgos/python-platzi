# Basico
print("Nunca pares de aprender")

# Coma
print("Nunca", "pares", "de", "aprender")

# Concatenar
print("Nunca" + "pares" + "de" + "aprender")
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# Sep: El parámetro sep permite especificar cómo separar los elementos al imprimir.
print("Nunca", "pares", "de", "aprender", sep="-")

# End: El parámetro end cambia lo que se imprime al final de la llamada a print.
print("Nunca", end=" ")
print("pares de aprender")

# Variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

# f-strings
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")

# format
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))
print("Frase: {f}, Autor: {a}".format(f=frase, a=author))

# Impresión con formato específico: Puedes controlar el formato de los números al imprimir.
valor = 3.14159
print("Valor: {:.2f}".format(valor))

# Para imprimir una cadena que contenga comillas simples o dobles dentro de ellas, debes usar secuencias de escape para evitar confusiones con la sintaxis de Python
print('Hola soy \'Carli\'')

# Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas, también necesitarás usar secuencias de escape para evitar que Python interprete las barras invertidas como parte de secuencias de escape
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")

# Operadores numericos
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicacion:", a * b)
print("Potenciacion:", a ** b)
print("Division:", a / b)
print("Parte entera de la Division:", a // b)
print("Modulo, resto de division:", a % b)

a += 2  # a = a + 2  -> +, -, *, /
print(a)

print('\n')

# Orden de operaciones: Paréntesis, Exponenciación, Multiplicación, División, Adición, Sustracción
operation_1 = 2 + 3 * 4
operation_2 = 2 + (3 * 4)

print(operation_1)
print(operation_2)

"""
Siguiendo el orden:

1. Paréntesis
(2 + 3) = 5
(4 ** 2) = 16

2. Multiplicacion
5 * 16 = 80

3. Division
80/8 = 10

4. Resta
10 - 1 = 9

Resultado = 9.0
"""
operation_3 = (2 + 3) * (4 ** 2) / 8 - 1
print(operation_3)

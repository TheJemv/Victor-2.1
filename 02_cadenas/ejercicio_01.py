"""
Ejercicio 1. Cadenas

Planteamiento:
    Preguntar el nombre del usuario y un número entero, e imprimir el nombre
    en líneas distintas tantas veces como indique el número.

Explicación:
    El número se convierte a int. Al nombre se le agrega un salto de línea
    ("\n") y se usa el operador de repetición de cadenas (*) para repetirlo
    n veces. Se usa end="" en print() para no dejar una línea vacía extra
    al final.
"""

nombre = input("¿Cómo te llamas? ")
n = int(input("Introduce un número entero: "))

print((nombre + "\n") * n, end="")

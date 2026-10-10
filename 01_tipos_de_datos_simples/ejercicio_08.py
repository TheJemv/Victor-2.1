"""
Ejercicio 8. Tipos de Datos Simples

Planteamiento:
    Pedir dos números enteros y mostrar <n> entre <m> da un cociente <c> y
    un resto <r>, donde c y r son el cociente y el resto de la división
    entera.

Explicación:
    Los datos se convierten a int. El operador // obtiene el cociente de la
    división entera y el operador % obtiene el resto (módulo). El mensaje se
    arma con un f-string que inserta los valores de las variables.
"""

n = int(input("Introduce el dividendo (número entero): "))
m = int(input("Introduce el divisor (número entero): "))

c = n // m
r = n % m

print(f"{n} entre {m} da un cociente {c} y un resto {r}")

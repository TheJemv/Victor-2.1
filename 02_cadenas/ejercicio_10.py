"""
Ejercicio 10. Cadenas

Planteamiento:
    Preguntar los productos de una cesta de la compra separados por comas y
    mostrar cada producto en una línea distinta.

Explicación:
    split(",") separa la cadena en una lista de productos usando la coma
    como separador. Un ciclo for recorre la lista y strip() quita los
    espacios sobrantes antes de imprimir cada producto en su propia línea.
"""

productos = input("Introduce los productos de la cesta separados por comas: ")

for producto in productos.split(","):
    print(producto.strip())

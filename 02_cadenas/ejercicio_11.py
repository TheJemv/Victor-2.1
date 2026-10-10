"""
Ejercicio 11. Cadenas

Planteamiento:
    Preguntar el nombre de un producto, su precio y un número de unidades, y
    mostrar una cadena con el nombre, el precio unitario con 6 dígitos
    enteros y 2 decimales, las unidades con 3 dígitos y el costo total con
    8 dígitos enteros y 2 decimales.

Explicación:
    Se usan f-strings con especificadores de formato que rellenan con ceros:
      - {precio:09.2f}: ancho total 9 = 6 enteros + punto + 2 decimales.
      - {unidades:03d}: entero con 3 dígitos.
      - {total:011.2f}: ancho total 11 = 8 enteros + punto + 2 decimales.
"""

producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

total = precio * unidades

print(f"{producto}: ${precio:09.2f} x {unidades:03d} = ${total:011.2f}")

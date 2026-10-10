"""
Ejercicio 4. Cadenas

Planteamiento:
    Los teléfonos de una empresa tienen el formato prefijo-número-extensión,
    con prefijo +52 y extensión de dos dígitos (por ejemplo
    +52-913724710-56). Pedir un teléfono con ese formato y mostrar solo el
    número, sin el prefijo ni la extensión.

Explicación:
    Se usa el rebanado (slicing) de cadenas. El prefijo "+52-" ocupa los
    índices 0 a 3, así que el número empieza en el índice 4. La extensión
    "-56" son los últimos 3 caracteres, por eso el corte termina en -3.
    telefono[4:-3] devuelve solo la parte central.
"""

telefono = input("Introduce un número de teléfono (formato +52-XXXXXXXXX-XX): ")

print("Número sin prefijo ni extensión:", telefono[4:-3])

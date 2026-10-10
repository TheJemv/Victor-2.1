"""
Ejercicio 9. Cadenas (versión con formato fijo dd/mm/aaaa)

Planteamiento:
    Preguntar la fecha de nacimiento en formato dd/mm/aaaa y mostrar el día,
    el mes y el año.

Explicación:
    Como el formato es fijo, cada parte ocupa siempre las mismas posiciones:
    el día los índices 0-1, el mes los índices 3-4 y el año desde el índice
    6. Se obtienen con rebanado de cadenas. Esta versión falla si el día o
    el mes tienen un solo dígito; la versión adaptada está en
    ejercicio_09_adaptado.py.
"""

fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia = fecha[:2]
mes = fecha[3:5]
anio = fecha[6:]

print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)

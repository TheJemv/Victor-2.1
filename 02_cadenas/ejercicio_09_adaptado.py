"""
Ejercicio 9. Cadenas (versión adaptada)

Planteamiento:
    Adaptar el programa anterior para que también funcione cuando el día o
    el mes se escriben con un solo carácter (por ejemplo 5/3/2004).

Explicación:
    En lugar de usar posiciones fijas, split("/") separa la fecha en una
    lista usando la diagonal como separador, sin importar cuántos dígitos
    tenga cada parte. Los tres elementos de la lista se asignan a dia, mes y
    anio en una sola línea (desempaquetado).
"""

fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, anio = fecha.split("/")

print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)

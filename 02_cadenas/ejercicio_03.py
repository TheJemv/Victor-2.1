"""
Ejercicio 3. Cadenas

Planteamiento:
    Preguntar el nombre del usuario y mostrar <NOMBRE> tiene <n> letras,
    donde <NOMBRE> es el nombre en mayúsculas y <n> el número de letras.

Explicación:
    strip() quita los espacios al inicio y al final de lo que se escribió.
    upper() convierte el nombre a mayúsculas y len() cuenta sus caracteres;
    antes se quitan los espacios intermedios con replace(" ", "") para que
    solo se cuenten letras. str() convierte el número a texto para
    concatenarlo.
"""

nombre = input("¿Cómo te llamas? ").strip()

letras = len(nombre.replace(" ", ""))

print(nombre.upper() + " tiene " + str(letras) + " letras")

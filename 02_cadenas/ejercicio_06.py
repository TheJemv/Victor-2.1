"""
Ejercicio 6. Cadenas

Planteamiento:
    Pedir una frase y una vocal, y mostrar la misma frase pero con esa vocal
    en mayúscula.

Explicación:
    La vocal se pasa a minúscula con lower() para que funcione aunque el
    usuario la escriba en mayúscula. Después replace() sustituye cada
    aparición de la vocal por su versión en mayúscula (upper()).
"""

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ").lower()

print(frase.replace(vocal, vocal.upper()))

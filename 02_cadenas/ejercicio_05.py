"""
Ejercicio 5. Cadenas

Planteamiento:
    Pedir una frase y mostrarla invertida.

Explicación:
    Se usa el rebanado con paso negativo: frase[::-1] recorre la cadena
    desde el último carácter hasta el primero y devuelve una cadena nueva
    con el orden invertido.
"""

frase = input("Introduce una frase: ")

print(frase[::-1])

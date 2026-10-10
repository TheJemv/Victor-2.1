"""
Ejercicio 3. Tipos de Datos Simples

Planteamiento:
    Preguntar el nombre del usuario y mostrar ¡Hola <nombre>!, donde
    <nombre> es el nombre que el usuario introdujo.

Explicación:
    input() muestra una pregunta y devuelve como cadena (str) lo que escribe
    el usuario. Ese valor se guarda en la variable nombre y se une con otras
    cadenas mediante el operador de concatenación (+) para formar el saludo.
"""

nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "!")

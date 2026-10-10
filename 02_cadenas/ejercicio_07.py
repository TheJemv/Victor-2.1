"""
Ejercicio 7. Cadenas

Planteamiento:
    Preguntar el correo electrónico del usuario y mostrar otro correo con el
    mismo nombre (la parte antes de la @) pero con el dominio
    utmatamoros.edu.mx.

Explicación:
    split("@") separa el correo en una lista usando la arroba como
    separador; el elemento [0] es el nombre de usuario. Ese nombre se
    concatena con "@utmatamoros.edu.mx" para formar el nuevo correo.
"""

correo = input("Introduce tu correo electrónico: ")

usuario = correo.split("@")[0]

print(usuario + "@utmatamoros.edu.mx")

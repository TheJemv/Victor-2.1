"""
Ejercicio 2. Cadenas

Planteamiento:
    Preguntar el nombre completo del usuario y mostrarlo tres veces: todo en
    minúsculas, todo en mayúsculas y con solo la primera letra del nombre y
    de los apellidos en mayúscula, sin importar cómo lo haya escrito.

Explicación:
    Se usan tres métodos de las cadenas: lower() convierte todo a
    minúsculas, upper() a mayúsculas y title() pone en mayúscula la primera
    letra de cada palabra y el resto en minúsculas.
"""

nombre = input("¿Cuál es tu nombre completo? ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())

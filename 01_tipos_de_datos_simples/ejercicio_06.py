"""
Ejercicio 6. Tipos de Datos Simples

Planteamiento:
    Leer un entero positivo n y mostrar la suma de todos los enteros desde
    1 hasta n, usando la fórmula suma = n(n + 1) / 2.

Explicación:
    El dato se convierte a entero con int(). Se aplica la fórmula de la suma
    de los n primeros enteros positivos; se usa la división entera (//)
    porque n(n + 1) siempre es par y así el resultado se mantiene como int.
"""

n = int(input("Introduce un número entero positivo: "))

suma = n * (n + 1) // 2

print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")

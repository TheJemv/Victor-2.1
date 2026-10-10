"""
Ejercicio 11. Tipos de Datos Simples

Planteamiento:
    Una cuenta de ahorros da 4% de interés al año, que se suma al balance
    al final de cada año. Leer la cantidad depositada y mostrar los ahorros
    tras el primer, segundo y tercer año, redondeados a dos decimales.

Explicación:
    La tasa se guarda en la constante INTERES. Cada año el balance se
    multiplica por (1 + INTERES), partiendo del balance del año anterior.
    El formato :.2f de los f-strings redondea cada cantidad a dos decimales
    y siempre muestra ambos (por ejemplo 1040.00).
"""

INTERES = 0.04

cantidad = float(input("¿Cantidad depositada en la cuenta? "))

ahorro_1 = cantidad * (1 + INTERES)
ahorro_2 = ahorro_1 * (1 + INTERES)
ahorro_3 = ahorro_2 * (1 + INTERES)

print(f"Ahorros tras el primer año: ${ahorro_1:.2f}")
print(f"Ahorros tras el segundo año: ${ahorro_2:.2f}")
print(f"Ahorros tras el tercer año: ${ahorro_3:.2f}")

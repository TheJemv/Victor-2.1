"""
Ejercicio 10. Tipos de Datos Simples

Planteamiento:
    Una juguetería vende payasos (112 g cada uno) y muñecas (75 g cada una).
    Leer el número de payasos y de muñecas del último pedido y calcular el
    peso total del paquete que será enviado.

Explicación:
    Los pesos unitarios se guardan en constantes (variables en mayúsculas
    que no cambian). Las cantidades se convierten a int y el peso total se
    obtiene multiplicando cada cantidad por su peso y sumando ambos
    resultados. También se muestra en kilogramos dividiendo entre 1000.
"""

PESO_PAYASO = 112
PESO_MUNECA = 75

payasos = int(input("Número de payasos vendidos: "))
munecas = int(input("Número de muñecas vendidas: "))

peso_total = payasos * PESO_PAYASO + munecas * PESO_MUNECA

print(f"El peso total del paquete es {peso_total} g ({peso_total / 1000} kg)")

"""
Ejercicio 7. Tipos de Datos Simples

Planteamiento:
    Pedir al usuario su peso (kg) y su estatura (m), calcular el índice de
    masa corporal (IMC), guardarlo en una variable y mostrar la frase
    Tu índice de masa corporal es <imc>, redondeado a dos decimales.

Explicación:
    Los datos se convierten a float. El IMC se calcula como
    peso / estatura ** 2 y se guarda en la variable imc. La función round()
    redondea el resultado a dos decimales y str() lo convierte a texto para
    poder concatenarlo con la frase.
"""

peso = float(input("¿Cuál es tu peso en kg? "))
estatura = float(input("¿Cuál es tu estatura en metros? "))

imc = peso / estatura ** 2

print("Tu índice de masa corporal es " + str(round(imc, 2)))

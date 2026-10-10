"""
Ejercicio 9. Tipos de Datos Simples

Planteamiento:
    Preguntar una cantidad a invertir, el interés anual y el número de años,
    y mostrar el capital obtenido en la inversión.

Explicación:
    Se usa la fórmula del interés compuesto:
        capital = cantidad * (1 + interes / 100) ** anios
    El interés se pide en porcentaje, por eso se divide entre 100. La
    cantidad y el interés son float y los años son int. El resultado se
    muestra con dos decimales.
"""

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés anual (%)? "))
anios = int(input("¿Número de años? "))

capital = cantidad * (1 + interes / 100) ** anios

print(f"El capital obtenido es: ${capital:.2f}")

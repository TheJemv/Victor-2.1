"""
Ejercicio 12. Tipos de Datos Simples

Planteamiento:
    Una panadería vende barras de pan a $3.49. El pan que no es del día
    tiene un descuento del 60%. Leer el número de barras vendidas que no son
    del día y mostrar el precio habitual de una barra, el descuento por no
    ser fresca y el costo final total.

Explicación:
    El precio y el porcentaje de descuento se guardan en constantes. El
    descuento por barra es PRECIO * DESCUENTO y el costo final es el número
    de barras por el precio ya descontado. Los montos se muestran con dos
    decimales usando el formato :.2f de los f-strings.
"""

PRECIO = 3.49
DESCUENTO = 0.60

barras = int(input("Número de barras vendidas que no son del día: "))

descuento_barra = PRECIO * DESCUENTO
costo_total = barras * (PRECIO - descuento_barra)

print(f"Precio habitual de una barra: ${PRECIO:.2f}")
print(f"Descuento por no ser fresca: {DESCUENTO * 100:.0f}% (${descuento_barra:.2f} por barra)")
print(f"Costo final total: ${costo_total:.2f}")

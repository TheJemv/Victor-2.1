"""
Ejercicio 8. Cadenas

Planteamiento:
    Preguntar el precio de un producto en euros con dos decimales y mostrar
    el número de euros y el número de céntimos.

Explicación:
    El precio se trabaja como cadena. find(".") devuelve la posición del
    punto decimal; con rebanado se toma lo que está antes del punto (euros)
    y lo que está después (céntimos).
"""

precio = input("Introduce el precio del producto en euros (con dos decimales): ")

punto = precio.find(".")
euros = precio[:punto]
centimos = precio[punto + 1:]

print(euros, "euros y", centimos, "céntimos")

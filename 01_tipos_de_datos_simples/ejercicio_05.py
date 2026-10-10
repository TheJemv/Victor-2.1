"""
Ejercicio 5. Tipos de Datos Simples

Planteamiento:
    Preguntar al usuario el número de horas trabajadas y el costo por hora,
    y mostrar la paga que le corresponde.

Explicación:
    input() siempre devuelve texto, por eso se convierte cada dato a número
    decimal con float(). La paga se obtiene multiplicando horas por costo
    (operador *) y se muestra con dos decimales usando un f-string.
"""

horas = float(input("¿Cuántas horas trabajaste? "))
costo = float(input("¿Cuál es el costo por hora? "))

paga = horas * costo

print(f"Tu paga es: ${paga:.2f}")

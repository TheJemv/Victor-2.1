# Victor-2.1

**Actividad 2.1: Ejercicios de Python. Parte 1**

- **Universidad:** Universidad Tecnológica de Matamoros
- **Asignatura:** Automatización de Infraestructura Digital I
- **Profesor:** Victor Alejandro Galvan Guerra
- **Cuatrimestre:** Septiembre – Diciembre 2026
- **Unidad:** II. Diseño y desarrollo de software
- **Proyecto integrador:** Sistema de automatización y gestión de infraestructura de red

Ejercicios de introducción a Python: variables, tipos de datos, entrada y salida
de información, operaciones aritméticas, cadenas de texto y conversión de datos.

## Estructura

```
.
├── 01_tipos_de_datos_simples/   # Sección 4: Primeros programas en Python (12 ejercicios)
│   ├── ejercicio_01.py
│   ├── ...
│   └── ejercicio_12.py
└── 02_cadenas/                  # Sección 5: Trabajando con cadenas (11 ejercicios)
    ├── ejercicio_01.py
    ├── ...
    ├── ejercicio_09.py
    ├── ejercicio_09_adaptado.py # Ejercicio 9 adaptado para día/mes de un dígito
    ├── ejercicio_10.py
    └── ejercicio_11.py
```

Cada archivo empieza con un comentario de documentación (docstring) que incluye el
**planteamiento** del problema y la **explicación** del programa y de los elementos
de Python que usa.

## Cómo ejecutar

Se necesita Python 3.6 o más reciente. Desde la raíz del repositorio:

```bash
python3 01_tipos_de_datos_simples/ejercicio_01.py
```

```bash
python3 02_cadenas/ejercicio_04.py
```

## Índice de ejercicios

### 1. Tipos de datos simples

| # | Archivo | Tema |
|---|---------|------|
| 1 | [ejercicio_01.py](01_tipos_de_datos_simples/ejercicio_01.py) | Mostrar un mensaje con `print()` |
| 2 | [ejercicio_02.py](01_tipos_de_datos_simples/ejercicio_02.py) | Guardar un mensaje en una variable |
| 3 | [ejercicio_03.py](01_tipos_de_datos_simples/ejercicio_03.py) | Leer el nombre con `input()` y saludar |
| 4 | [ejercicio_04.py](01_tipos_de_datos_simples/ejercicio_04.py) | Operación aritmética `((3+2)/(2·5))²` |
| 5 | [ejercicio_05.py](01_tipos_de_datos_simples/ejercicio_05.py) | Paga por horas trabajadas |
| 6 | [ejercicio_06.py](01_tipos_de_datos_simples/ejercicio_06.py) | Suma de 1 a n con `n(n+1)/2` |
| 7 | [ejercicio_07.py](01_tipos_de_datos_simples/ejercicio_07.py) | Índice de masa corporal |
| 8 | [ejercicio_08.py](01_tipos_de_datos_simples/ejercicio_08.py) | Cociente y resto de la división entera |
| 9 | [ejercicio_09.py](01_tipos_de_datos_simples/ejercicio_09.py) | Capital de una inversión (interés compuesto) |
| 10 | [ejercicio_10.py](01_tipos_de_datos_simples/ejercicio_10.py) | Peso de un paquete de payasos y muñecas |
| 11 | [ejercicio_11.py](01_tipos_de_datos_simples/ejercicio_11.py) | Ahorros con 4% de interés anual a 3 años |
| 12 | [ejercicio_12.py](01_tipos_de_datos_simples/ejercicio_12.py) | Descuento de pan que no es del día |

### 2. Cadenas

| # | Archivo | Tema |
|---|---------|------|
| 1 | [ejercicio_01.py](02_cadenas/ejercicio_01.py) | Repetir el nombre n veces |
| 2 | [ejercicio_02.py](02_cadenas/ejercicio_02.py) | Minúsculas, mayúsculas y tipo título |
| 3 | [ejercicio_03.py](02_cadenas/ejercicio_03.py) | Contar las letras de un nombre |
| 4 | [ejercicio_04.py](02_cadenas/ejercicio_04.py) | Teléfono sin prefijo ni extensión |
| 5 | [ejercicio_05.py](02_cadenas/ejercicio_05.py) | Invertir una frase |
| 6 | [ejercicio_06.py](02_cadenas/ejercicio_06.py) | Poner una vocal en mayúscula |
| 7 | [ejercicio_07.py](02_cadenas/ejercicio_07.py) | Cambiar el dominio de un correo |
| 8 | [ejercicio_08.py](02_cadenas/ejercicio_08.py) | Separar euros y céntimos |
| 9 | [ejercicio_09.py](02_cadenas/ejercicio_09.py) / [ejercicio_09_adaptado.py](02_cadenas/ejercicio_09_adaptado.py) | Día, mes y año de una fecha |
| 10 | [ejercicio_10.py](02_cadenas/ejercicio_10.py) | Productos de una cesta en líneas distintas |
| 11 | [ejercicio_11.py](02_cadenas/ejercicio_11.py) | Formato de precio, unidades y total |

## Ejemplos de ejecución

### 1. Tipos de datos simples

```
$ python3 01_tipos_de_datos_simples/ejercicio_01.py
¡Hola estudiante de IRIC!

$ python3 01_tipos_de_datos_simples/ejercicio_02.py
¡Hola estudiante de IRIC!

$ python3 01_tipos_de_datos_simples/ejercicio_03.py
¿Cómo te llamas? Ana
¡Hola Ana!

$ python3 01_tipos_de_datos_simples/ejercicio_04.py
El resultado de la operación es: 0.25

$ python3 01_tipos_de_datos_simples/ejercicio_05.py
¿Cuántas horas trabajaste? 40
¿Cuál es el costo por hora? 85.5
Tu paga es: $3420.00

$ python3 01_tipos_de_datos_simples/ejercicio_06.py
Introduce un número entero positivo: 10
La suma de los enteros desde 1 hasta 10 es: 55

$ python3 01_tipos_de_datos_simples/ejercicio_07.py
¿Cuál es tu peso en kg? 70
¿Cuál es tu estatura en metros? 1.75
Tu índice de masa corporal es 22.86

$ python3 01_tipos_de_datos_simples/ejercicio_08.py
Introduce el dividendo (número entero): 17
Introduce el divisor (número entero): 5
17 entre 5 da un cociente 3 y un resto 2

$ python3 01_tipos_de_datos_simples/ejercicio_09.py
¿Cantidad a invertir? 10000
¿Interés anual (%)? 5
¿Número de años? 3
El capital obtenido es: $11576.25

$ python3 01_tipos_de_datos_simples/ejercicio_10.py
Número de payasos vendidos: 3
Número de muñecas vendidas: 4
El peso total del paquete es 636 g (0.636 kg)

$ python3 01_tipos_de_datos_simples/ejercicio_11.py
¿Cantidad depositada en la cuenta? 1000
Ahorros tras el primer año: $1040.00
Ahorros tras el segundo año: $1081.60
Ahorros tras el tercer año: $1124.86

$ python3 01_tipos_de_datos_simples/ejercicio_12.py
Número de barras vendidas que no son del día: 10
Precio habitual de una barra: $3.49
Descuento por no ser fresca: 60% ($2.09 por barra)
Costo final total: $13.96
```

### 2. Cadenas

```
$ python3 02_cadenas/ejercicio_01.py
¿Cómo te llamas? Ana
Introduce un número entero: 3
Ana
Ana
Ana

$ python3 02_cadenas/ejercicio_02.py
¿Cuál es tu nombre completo? maRÍa fernANDA lópez
maría fernanda lópez
MARÍA FERNANDA LÓPEZ
María Fernanda López

$ python3 02_cadenas/ejercicio_03.py
¿Cómo te llamas? Fernanda
FERNANDA tiene 8 letras

$ python3 02_cadenas/ejercicio_04.py
Introduce un número de teléfono (formato +52-XXXXXXXXX-XX): +52-913724710-56
Número sin prefijo ni extensión: 913724710

$ python3 02_cadenas/ejercicio_05.py
Introduce una frase: Hola mundo
odnum aloH

$ python3 02_cadenas/ejercicio_06.py
Introduce una frase: Automatizacion de infraestructura
Introduce una vocal: a
AutomAtizAcion de infrAestructurA

$ python3 02_cadenas/ejercicio_07.py
Introduce tu correo electrónico: alumno123@gmail.com
alumno123@utmatamoros.edu.mx

$ python3 02_cadenas/ejercicio_08.py
Introduce el precio del producto en euros (con dos decimales): 25.99
25 euros y 99 céntimos

$ python3 02_cadenas/ejercicio_09.py
Introduce tu fecha de nacimiento (dd/mm/aaaa): 05/03/2004
Día: 05
Mes: 03
Año: 2004

$ python3 02_cadenas/ejercicio_09_adaptado.py
Introduce tu fecha de nacimiento (dd/mm/aaaa): 5/3/2004
Día: 5
Mes: 3
Año: 2004

$ python3 02_cadenas/ejercicio_10.py
Introduce los productos de la cesta separados por comas: pan, leche, huevos, café
pan
leche
huevos
café

$ python3 02_cadenas/ejercicio_11.py
Nombre del producto: Router
Precio unitario: 1250.5
Número de unidades: 3
Router: $001250.50 x 003 = $00003751.50
```

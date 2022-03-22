# Práctica 1 - Parte I

Esta práctica tiene como objetivo poder volcar en lo práctico en Python lo visto en las clases 1 y 2.

_Escriban y prueben sus programas en: [Python Online](https://www.online-python.com/) y guardenlo en su computadora como un txt para posteriormente subirlo a Google Drive o donde prefieran. Mas adelante en el curso aprenderemos a usar [GitHub](https://github.com/) para guardar nuestro código._

## Ejercicio 1
Escribir un programa que imprima en pantalla `¡Hola Mundo!`.

_Nota: Utilice la instrucción_ `print()`

[Pista](https://kity-linuxero.github.io/prog_CFP410/clase2.html#/4)

## Ejercicio 2
Escribir un programa que almacene el string `¡Hola mundo!` en una variable y luego muestre en pantalla el contenido de la variable.

_Nota: Utilice la instrucción_ `print()`

[Pista](https://kity-linuxero.github.io/prog_CFP410/clase2.html#/4)

## Ejercicio 3
Escribir un programa que imprima en pantalla `¡Hola Mundo!` tres veces.

Pista: Puede usar las sentencias [while](https://kity-linuxero.github.io/prog_CFP410/clase1.html#/6/13) o [for](https://kity-linuxero.github.io/prog_CFP410/clase1.html#/6/14) vistas en clase

## Ejercicio 4
Siguiendo este ejemplo de programa que suma dos números:
```python
num1=1 # Asigno valor a número 1
num2=2 # Asigno valor a número 2
print("La suma es: ")
print(num1 + num2)
```
Escriba dos programas uno que reste los números y otro programa que los multiplique.

[Pista]("https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/7")


## Ejercicio 5
Escriba este programa en el intérprete online

```python
nombre= input("Ingrese su nombre: ") # Asignación a una variable de identificador "nombre"
print("Hola"+ nombre) # Concatenación
```
¿El programa funciona correctamente? ¿Haría algún cambio para mejorarlo?

## Ejercicio 6

Escriba un programa que pregunte el nombre y luego imprima en pantalla `"¡Hola, <Nombre>!"`. Respetar los signos de admiración.

Ejemplo:
```bash
Ingrese su nombre: Marcos

¡Hola Marcos!
```

[Pista](https://kity-linuxero.github.io/prog_CFP410/clase1.html#/5/2)


## Ejercicio 7
Escriba un programa que compare dos números y diga cual de los dos es el mayor. Ejemplo:
```bash
# Si se tienen numero1=2 y numero2=44
El numero 2 es mayor
```

```bash
# Si se tienen numero1=44 y numero2=11
El numero 1 es mayor
```

Pruebe con todos los números que se les ocurra para ver que el programa funciona correctamente.

Pista: Repase [Decisión](https://kity-linuxero.github.io/prog_CFP410/clase1.html#/6/7/1) y [Comparaciones entre tipos]("https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/13")

## Ejercicio 8
Escriba un programa que reciba por teclado dos números y los sume entre sí.

Por ejemplo:
```bash
Ingrese un número: 3
Ingrese otro número: 2
El resultado es:
5
```

_Nota: Los valores leídos por teclados siempre son string. Para sumarlos tendrá que hacer una conversión al tipo int. Ver la presentación tipos_

#### Ayuda:
Para guardar un entero leído desde teclado:
```python
str=input("Ingrese el valor: ")
numero = int(str)
```
Puede hacerlo en un paso de la siguiente manera:
```python
numero= int(input("Ingrese el valor: "))
```

Ambas formas están bien. Utilicen las que les sea mas fácil para entender el código. No porque sea mas compacta la instrucción es mejor.

## Ejercicio 9

Escribir un programa que pregunte cuántas horas trabajó y el coste por hora. Después debe mostrar por pantalla la paga que corresponde.

Ejemplo:
```bash
Horas trabajadas: 8
Coste por hora: 500
La paga correspondiente es:
4000
```

## Ejercicio 10
Escribir un programa que simule ser un cajero automático donde se extrae dinero de la cuenta. El programa debe consultar al usuario la cantidad que desea extraer. Si el dinero que desea extraer es menor al saldo total, la extracción será exitosa y deberá informar el monto extraído y el saldo restante.

Si se solicita un monto que excede el monto, el programa deberá decir saldo insuficiente.
Supongamos que se tiene en cuenta 1000.

```bash
Ingrese el monto a extraer:
200

Ha extraido:
200

Le queda en cuenta 800
```

En caso que quiera extraerse mas que el saldo disponible:
```bash
Ingrese el monto a extraer:
1200

No hay suficiente saldo para completar la operación
```

El monto en la cuenta está previamente cargado (no se ingresa por teclado).
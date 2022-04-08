# Práctica 3

En esta práctica trataremos de aplicar los conceptos de __modularización__ vistos en clase.


_Escriban y prueben sus programas en: [Python Online](https://www.online-python.com/) y guardenlo en su computadora como un txt o un py. Mas adelante en el curso aprenderemos a usar [GitHub](https://github.com/) para guardar nuestro código._


## Ejercicio 1

Escriba una función que reciba un nombre de una persona (ingresada por el usuario por teclado) y lo salude desde el módulo (no debe retornar nada). Por ejemplo, si le mandamos "Manuel" el módulo debe imprimir en pantalla: `¡Hola Manuel!`. Junto con la función, escribir el programa que invoque a la función.

## Ejercicio 2

Escriba una función que _retorne_ el cuadrado de un número _enviado por parámetro_. (Se debe multiplicar por si mismo ;)

## Ejercicio 3

Escriba una función que reciba dos números _y retorne_ el mayor de esos dos. Devolverlos con `return` e imprimirlo desde el programa

## Ejercicio 4

Escriba una función de nombre `esCero(unNumero)` que retorne _si_ un número es igual a 0 o no y úselo en el siguiente programa.

```python
if esCero(unNumero):
    print ("Es cero")
else:
    print ("No es cero")
```

Note lo legible que queda el programa principal :)

## Ejercicio 5

Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

Pista: Utilice parámetros por defecto. [Agregado en la clase 3]("https://kity-linuxero.github.io/prog_CFP410/clase3.html#3/11/0").

## Ejercicio 6

Escriba un programa que reciba una secuencia de números ingresada por teclado hasta que llegue un número negativo. Al finalizar el programa debe imprimir en pantalla el mayor y el menor de los números ingresados.

Pistas:
- Utilice modularización para separar las responsabilidades del programa.
- La función escrita en el ejercicio anterior le será muy útil en este ejercicio ;)
- En el primer ingreso de números, asigne a su máximo y mínimo el valor ingresado (Una opción posible) ó:
- Puede llevar la cuenta del máximo y mínimo con valores opuestos. Ponga el siguiente código al principio de su programa para llevar la cuenta de máximos y mínimos de esa forma (otra opción posible):

```python
min=99999999 # El mínimo se inicia en un número grande para que al ser comparado con el primero sea reemplazado
max=-1 # El máximo se inicializa en -1 para que cuando llegue el primer número máximo real este sea reemplazado
```

- Sugerencia
    - Una función para que _retorne_ el mayor entre dos
    - Una función para que _retorne_ el menor entre dos

## Ejercicio 7

Re escriba el programa hecho en la práctica 2, ejercicio 9 utilizando módulos:
>Escriba un programa que le pida al usuario que ingrese un número del 1 al 6 y simule la función que se lanza un dado... El programa debe seguir hasta que el usuario acerte el número.

Compare los dos programas. ¿Qué conclusión puede sacar?

Pistas:
- Escriba una función que se ocupe de retornar el valor elegido eleatoriamente del dado
- Escriba una función que se ocupe de saber si acertamos el dado.


## Ejercicio 8

Piense en el programa hecho del juego de piedra, papel y tijera de la práctica anterior [Ejercicio 10.1]("https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/practica2.md#ejercicio-101-solo-para-valientes-xd"). ¿Cómo podríamos separar responsabilidades para asignarles a los módulos?.

Imagínese todos los módulos que le ayude a tener un programa legible y ordenado. A continuación se dará algunos posibles módulos. No son obligatorios y úselos si realmente le ayuda a resolver el programa (ya que cada alumnx lo resolvió de forma diferente y puede variar la implementación).

Posibles módulos:
- Un módulo podría encargarse de recibir la opción que da el usuario y limpiar los datos incorrectos para finalmente devolverme un valor válido.
- Otro módulo puede encargase de la parte donde la computadora elige su opción.
- Otro módulo de saber si la opción elegida por el usuario le gana a la elegida por la computadora.

## Ejercicio 9
Modifique el programa de piedra, papel y tijera del ejercicio anterior para que permita a la computadora hacer trampa dándole la oportunidad de tirar otra vez en caso que el usuario haya ganado en el primer intento. El usuario no debe enterarse ;) y la PC podrá elegir solo una vez mas (sino sería muy obvio XD).











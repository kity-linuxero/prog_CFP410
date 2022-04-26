# Práctica 4

En esta práctica entederemos el uso práctico de __listas__ vistas en clase. Aplique todas las técnicas que hemos visto hasta ahora que considere necesarias. En los casos que pueda y considere __modularice__ la solución y agregue comentarios al programa para aumentar la legibilidad cuando sea leída por un tercero.


## Ejercicio 1

Escriba un programa que dada la lista `[1, 2, 3, 4, 5, 6, 7]` convierta cada elemento a su cuadrado `(n*n)` en una lista nueva y luego imprima por pantalla la nueva lista.

## Ejercicio 2

Escriba un programa que genere una lista de 100 elementos con números enteros aleatorios entre -1000 y 1000. Y luego informe la suma y el promedio de todos los elementos de la lista.

## Ejercicio 3

Escriba un programa que genere una lista con números consecutivos del 1 al 1000.

Una ayudita: [Uso de range]("https://www.programiz.com/python-programming/methods/built-in/range")

## Ejercicio 4

Escriba un programa que tome por teclado la temperatura media de cada día de la semana. Una vez tomados los datos que deben ser ingresados por teclado, debe informar la temperatura máxima y la mínima y qué día ocurrió cada una.

```bash
Ingrese temperatura media en el día domingo: 23.4
Ingrese temperatura media en el día lunes: 21.0
Ingrese temperatura media en el día martes: 18.3
Ingrese temperatura media en el día miercoles: 16.4
Ingrese temperatura media en el día jueves: 17.9
Ingrese temperatura media en el día viernes: 15.6
Ingrese temperatura media en el día sábado: 15.4

La máxima se dió el día domingo, con 23.4 ºC
La mínima se dió el día sábado, con 15.4 ºC
```

Pista:
- Haga una lista con los días de la semana e itere sobre esa lista.


## Ejercicio 5

Dada la lista `[10, 20, [300, 400, [5000, 6000], 500], 30, 40]` escriba un programa que modifique esa lista e imprima en pantalla la siguiente lista `[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]`.


## Ejercicio 6

Escriba un programa que permita escribir una lista de n palabras. Al inicio del programa se le preguntará al usuario la cantidad de palabras que va a ingresar y luego se ingresarán ese número de palabras por teclado.

Al final debe imprimir la lista de palabras en orden alfabético.

```bash
Ingrese el número de palabras que desea procesar: 6
Ingrese palabra 1: Trenes
Ingrese palabra 2: Camiones
Ingrese palabra 3: Tractores
Ingrese palabra 4: Barcos
Ingrese palabra 5: Aviones
Ingrese palabra 6: Peaones

La lista es: ['Aviones', 'Barcos', 'Camiones', 'Peatones', 'Tractores', 'Trenes']

```

## Ejercicio 7

Modifique el programa anterior agregando la opción de _cuenta palabras_. Al finalizar el programa y luego de imprimir la lista pregunte qué palabra le gustaría buscar en la lista. Luego debe contar la cantidad de veces que aparece dicha palabra.

```bash
Ingrese el número de palabras que desea procesar: 7
Ingrese palabra 1: Trenes
Ingrese palabra 2: Camiones
Ingrese palabra 3: Tractores
Ingrese palabra 4: Barcos
Ingrese palabra 5: Aviones
Ingrese palabra 6: Peaones
Ingrese palabra 7: Barcos

La lista es: ['Aviones', 'Barcos', 'Barcos', 'Camiones', 'Peatones', 'Tractores', 'Trenes']

Ingrese la palabra que desea buscar: Barcos

La palabra Barcos aparece 2 veces

```

## Ejercicio 8

Modifique el programa anterior para que el programa contenga una lista predefinida por el programador de palabras no válidas o prohibidas para ingresar.

```bash
Ingrese el número de palabras que desea procesar: 7
Ingrese palabra 1: Trenes
Ingrese palabra 2: Camiones
Ingrese palabra 3: Tractores
Ingrese palabra 4: Gatos
La palabra "Gatos" está en la lista de palabras prohibidas. Por favor elija otra.
Ingrese palabra 4: Aviones
Ingrese palabra 5: Peaones
.......

```

## Ejercicio 9

Escriba un programa que genere un sorteo para el juego del "amigx invisible". Donde se ingresan los nombres de las personas que participan y a cada uno se le asigna otra persona la cual será su amigx invisible. En caso que las personas sean número impar, complete con el profesor para que nadie se quede sin su amigx invisible. Lo usaremos mas adelante cuando hagamos el _tester invisible_ XD.


## Ejercicio 10

Escriba un programa que reciba la apuesta de n jugadores. A los jugadores se les pregunta el nombre y el número al cual apuestan. Las apuestas son números entre 0 y 99 y puede ser que varios jugadores apuesten al mismo número. Una vez que todos los jugadores hayan realizado su apuesta, el programa sortea un número entre 0 y 99. Puede ser que no haya ganadores, o haya mas de uno. Debe informar si hay ganadores o no y debe decir el nombre de los ganadores.

### Ejemplo

```bash
Ingrese nombre de la/el apostador: Martín
Ingrese su apuesta: 89

Ingrese nombre de la/el apostador: Agustin
Ingrese su apuesta: 19

Ingrese nombre de la/el apostador: Rebeca
Ingrese su apuesta: 76

Ingrese nombre de la/el apostador: Patricio
Ingrese su apuesta: 0

Ingrese nombre de la/el apostador: Fernanda
Ingrese su apuesta: 99

Ingrese nombre de la/el apostador: . # Termina de tomar apuestas

Salió sorteado el número 86. No hay ganadores

```

## Ejercicio 11

### Ejercicio para super sayayins de la programación XD


>Este ejercicio tiene una dificultad alta. Necesitará pensar cada parte del programa. Modularice cada parte del programa de manera que pueda reutilizar el código que se utilizará en cada turno. ¡Éxitos!

Escriba un programa que permita jugar _una especie_ de __"7 y medio"__ que se juega con mazos de cartas españolas. Las cartas españolas tiene cuatro palos: espada, basto, copa y oro y cada palo tiene cartas numeradas del 1-12. A efectos del ejercicio eliminaremos las cartas 8 y 9 de cada palo, quedando 10 cartas por palo y en total 40 cartas.

Al principio del programa, se le preguntará la cantidad de jugadores que deseen jugar. Siendo el mínimo 2 jugadores (la pc no jugará).

Para este juego, no importa el palo de la carta, pero sí el valor numérico. Las cartas del 1 al 7 valen del 1 al 7 respectivamente. Los 10,11 y 12 valen 1/2.

El juego consiste en que el jugador pide cartas a la computadora y luego de pedir una carta elegir si se "planta" o quiere otra carta mas. Gana el jugador que llegue mas cerca de sacar 7 y 1/2. Pero pierde automáticamente cuando se pasa.

A tener en cuenta. Al principio de la partida debe _barajarse_ las cartas quedando mezcladas. A medida que un jugador pida una carta, la carta es quitada del mazo.

Ejemplo de juego:

```bash
¡Bienvenidx al juego de cartas 7 y medio del curso de programación del CFP!

Elija la cantidad de jugadores (mínimo 2): 3

Turno jugador 1-
Su carta en este turno es: 5
En total lleva 5 puntos.
¿Desea sacar otra carta? (S/n): s
Su carta en este turno es: 10
En total lleva 5,5 puntos.
¿Desea sacar otra carta? (S/n): s
Su carta en este turno es: 1
En total lleva 6,5 puntos.
¿Desea sacar otra carta? (S/n): n
El jugador 1 terminó su partida con 6,5.
--------------
Turno jugador 2
Su carta es: 2
En total lleva 2 puntos.
¿Desea sacar otra carta? (S/n): s
Salió una carta 7.
¡Perdiste!
El jugador 2 terminó su partida con 9.
--------------
Turno jugador 3
Su carta es: 7
En total lleva 7 puntos.
¿Desea sacar otra carta? (S/n): n
El jugador 3 terminó su partida con 7.
--------------
¡Ganó jugador 3!
```

Sugerencias (Son opcionales pero le puede ayudar a resolver el ejercicio)
- Escriba un módulo que, dada una carta le devuelva el valor de la misma.
- Escriba un módulo que le permita saber si un jugador se pasó del puntaje o no. Lo que indicaría si perdió o no.
- Escriba un módulo para crear el mazo.
- Escriba un módulo para barajar las cartas (mezclarlas)
- El mazo de cartas puede ser una lista. Como no importa el palo podrá resolverlo con una lista de 40 elementos numéricos. Debe haber 4 elementos de cada número 1,2,3,4,5,6,7,10,11 y 12.
- Vaya probando cada módulo a medida que los vaya escribiendo. Por ejemplo. Cuando haga el módulo para crear el mazo, imprima con `print()`el mazo creado para verificar que funciona. Una vez creado el mazo pruebe con `print()`si al mezclarlo, el mismo se hace correctamente.





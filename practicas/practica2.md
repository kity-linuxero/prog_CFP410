# Práctica 2

Esta práctica es la continuación de la [Práctica 1](https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/practica1.md) y tiene como objetivo poder volcar en lo práctico en Python lo visto en las clases 1 y 2.


_Escriban y prueben sus programas en: [Python Online](https://www.online-python.com/) y guardenlo en su computadora como un txt para posteriormente subirlo a Google Drive o donde prefieran. Mas adelante en el curso aprenderemos a usar [GitHub](https://github.com/) para guardar nuestro código._


## Ejercicio 1
Escriba un programa que devuelva si un caracter determinado es una vocal o no. El caracter puede estar predefinido o ingresarlo por teclado. Es a libre elección del alumnx ;).

Pista:
- Puede usar un `case` [visto en clase]("https://kity-linuxero.github.io/prog_CFP410/clase1.html#/case/1")
- O una serie de `if` anidados [vistos en clase]("https://kity-linuxero.github.io/prog_CFP410/clase1.html#/6/10")

## Ejercicio 2
Escriba un programa que, ingresado un número diga si es par o impar.

Pista: El [módulo](https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/6) del número y 2 debe ser 0.


## Ejercicio 3
Escriba un programa que lea por teclado nombres de personas hasta que llega "Juan". En el momento que llega "Juan" el programa debe informar la cantidad de personas que llegaron.

Ejemplo:
```bash
Ingrese el nombre de una persona:
Marcos
Ingrese el nombre de una persona:
Franco
Ingrese el nombre de una persona:
Celeste
Ingrese el nombre de una persona:
Juan
Llegaron 4 personas
```

Pista:
- [Compare los strings](https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/13) y que la condición de corte de la [iteración](https://kity-linuxero.github.io/prog_CFP410/clase1.html#/6/11/1) sea que el nombre ingresado es "Juan"
- Contabilice de alguna manera la cantidad de presonas que fueron ingresando.

## Ejercicio 4

Escribir un programa que procese todos los números ingresados hasta que se ingrese el valor "." (punto). En ese momento el programa termina en la iteración y deberá informar __la suma de todos los números ingresados__.

Ejemplo
```bash
Ingrese un número:
2
Ingrese un número:
3
Ingrese un número:
5
Ingrese un número:
.
La suma es 10.
```

Pistas:
- Debe convertir los valores ingresados [(string) a int]("https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/20").
- Tenga una variable para ir totalizando las sumas

## Ejercicio 5

Modifique el programa anterior para que tenga la capacidad de calcular __el promedio de los números ingresados__.

Ejemplo
```bash
Ingrese un número:
2
Ingrese un número:
3
Ingrese un número:
5
Ingrese un número:
.
La suma es 10.
El promedio es: 3.33333...
```

Pistas:
- Contabilice la cantidad de números que fueron ingresando.
- Para el promedio divida el valor de la suma total con la cantidad de números ingresados. 


## Ejercicio 6 

Escriba un programa que espere un número ingresado `n` por el usuario e imprima en pantalla la suma de los primeros `n números` naturales.
Por ejemplo, si se ingresa el número 5, el programa debe imprimir en pantalla la suma de : `1+2+3+4+5`.

```bash
Ingrese un número: 5

La suma es 15
```

Realizar dos versiones para este programa:

- Hacerlo con iteraciones y teniendo un contador.

- Mejorar el programa y realizar la suma de los primeros n números naturales fórmula matemática: `(n*(n+1))/2`

![Formula](https://static.wixstatic.com/media/2410c5_4a2f52e9c31740eba39ab8713e39ba2b~mv2.png/v1/fill/w_193,h_143,al_c,lg_1,enc_auto/2410c5_4a2f52e9c31740eba39ab8713e39ba2b~mv2.png)

Pista: Las operaciones entre números soportan paréntesis para dividir términos.


## Ejercicio 7
Escriba un programa que calcule si una o un alumno puede promocionar una materia.
Una materia consta de 3 examenes y el promedio para promocionar debe ser >= 8 pero si en algún exámen hay una nota < 6 la o el alumno no prodrá promocionar por mas que el promedio sea >= 8.
Las notas son de 1 a 10.

Ejemplo que no promociona:
```
Ingrese la nota en el primer exámen: 6
Ingrese la nota en el segundo exámen: 8
Ingrese la nota en el tercer exámen: 8
Resultado: La o el alumno NO promocionó la materia :(

# Da como promedio < 8

```

Ejemplo que tampoco promociona:
```
Ingrese la nota en el primer exámen: 10
Ingrese la nota en el segundo exámen: 10
Ingrese la nota en el tercer exámen: 5
Resultado: La o el alumno NO promocionó la materia :(

# Da como promedio > 8 pero tuvo una nota < 6

```

Ejemplo que sí promociona:
```
Ingrese la nota en el primer exámen: 8
Ingrese la nota en el segundo exámen: 10
Ingrese la nota en el tercer exámen: 8
Resultado: ¡La o el alumno promocionó la materia! :D

# Da como promedio >= 8

```

## Ejercicio 8
Copie y pegue este programa en el [interprete Python]("https://www.online-python.com/") y analice el código. ¿Qué hace el mismo?

```python
import random

num = random.randint(0, 99)
print (num)
```

## Ejercicio 9
Escriba un programa que le pida al usuario que ingrese un número del 1 al 6 y simule la función que se lanza un dado usando como ejemplo el ejercicio anterior. El programa debe seguir hasta que el usuario acerte el número.

## Ejercicio 10
Siguiendo los ejemplos anteriores escriba un juego para jugar piedra, papel o tijeras.

Ejemplos:

```bash
Elija una opción:
1) Piedra
2) Papel
3) Tijera.

Su opción: 3

¡Perdiste! Yo elegí piedra XD
```

```bash
Elija una opción:
1) Piedra
2) Papel
3) Tijera.

Su opción: 3

¡Ganaste! Yo elegí papel :(
```

# Ejercicio 10.1 (solo para valientes! XD)
Modificar el programa anterior de piedra, papel y tijera de manera que se juegue varias veces (hasta que el usuario decida no jugar mas) y una vez terminado cuente la cantidad de victorias y derrotas que tuvo con respecto a la computadora.





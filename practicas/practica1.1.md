# Práctica 1 - Parte II

Esta práctica tiene como objetivo poder volcar en lo práctico en Python lo visto en las clases 1 y 2.

_Escriban y prueben sus programas en: [Python Online](https://www.online-python.com/) y guardenlo en su computadora como un txt para posteriormente subirlo a Google Drive o donde prefieran. Mas adelante en el curso aprenderemos a usar [GitHub](https://github.com/) para guardar nuestro código._


## Ejercicio 1
Escriba un programa que devuelva si un caracter determinado es una vocal o no. El caracter puede estar predefinido o ingresarlo por teclado. Es a libre elección del alumnx ;).

## Ejercicio 2
Escriba un programa que, ingresado un número diga si es par o impar.
Pista: El [módulo](https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/7) debe ser 0.


## Ejercicio 3
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
- Debe convertir los valores ingresados (string) a int.
- Tenga una variable para ir totalizando las sumas

## Ejercicio 4

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

## Ejercicio 5
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

Pista: [Compare los strings](https://kity-linuxero.github.io/prog_CFP410/clase2.html#/3/13) y que la condición de corte de la [iteración](https://kity-linuxero.github.io/prog_CFP410/clase1.html#/6/11/1) sea que el nombre ingresado es "Juan"

## Ejercicio 6 

Escriba un programa que espere un número ingresado `n` por el usuario e imprima en pantalla la suma de los primeros `n números` naturales.
Por ejemplo, si se ingresa el número 5, el programa debe imprimir en pantalla la suma de : `1+2+3+4+5`.

```bash
Ingrese un número: 5

La suma es 15
```

- Hacerlo con iteraciones y teniendo un contador.

- Mejorar el programa y realizar la suma de los primeros n números naturales fórmula matemática $\frac{n(n+1)}{2}$

Pista: Las operaciones entre números soportan paréntesis para dividir términos.


## Ejercicio 7
Escriba un programa que calcule si una o un alumno puede promocionar una materia.
Una materia consta de 3 examenes y el promedio para promocionar debe ser >= 8 pero si en algún exámen hay una nota < 6 la o el alumno no prodrá promocionar por mas que el promedio sea >= 8.
Las notas son de 1 a 10.

Ejemplo que no promociona:
```
Ingrese la nota en el primer exámen: 6
Ingrese la nota en el primer exámen: 8
Ingrese la nota en el primer exámen: 8
Resultado: La o el alumno NO promociona la materia

# Da como promedio < 8

```

Ejemplo que tampoco promociona:
```
Ingrese la nota en el primer exámen: 10
Ingrese la nota en el primer exámen: 10
Ingrese la nota en el primer exámen: 5
Resultado: La o el alumno NO promociona la materia

# Da como promedio > 8 pero tuvo una nota < 6

```

Ejemplo que sí promociona:
```
Ingrese la nota en el primer exámen: 8
Ingrese la nota en el primer exámen: 10
Ingrese la nota en el primer exámen: 8
Resultado: ¡La o el alumno promocionó!

# Da como promedio >= 8

```

## Ejercicio 8
Basandose en el ejercicio anterior, escriba un programa que reciba la nota de los dos primeros exámenes y calcule que nota deberá tener en el tercer y último exámen para poder promocionar la materia si es que aún tiene posibilidades de hacerlo.

Ejemplo si no promociona:
```
Ingrese la nota en el primer exámen: 6
Ingrese la nota en el primer exámen: 6

Resultado: La o el alumno NO podrá promocionar la materia. Porque el promedio no alcanza.

# Ya que por mas que obtenga un 10 en el último exámen, dará como promedio 7.33 que es < 8

```

Ejemplo si aún puede promocionar:
```
Ingrese la nota en el primer exámen: 8
Ingrese la nota en el primer exámen: 10

Resultado: ¡La o el alumno promocionó!

# Da como promedio >= 8

```

Pista ;)

$\frac{n1+n2+n3}{3}>=8$

$\ x>=8*3-n1-n2$




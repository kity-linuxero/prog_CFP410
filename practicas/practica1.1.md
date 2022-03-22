# Práctica 1 - Parte II

Esta práctica tiene como objetivo poder volcar en lo práctico en Python lo visto en las clases 1 y 2.

_Escriban y prueben sus programas en: [Python Online](https://www.online-python.com/) y guardenlo en su computadora como un txt para posteriormente subirlo a Google Drive o donde prefieran. Mas adelante en el curso aprenderemos a usar [GitHub](https://github.com/) para guardar nuestro código._


## Ejercicio 1
Escriba un programa que devuelva si un caracter determinado es una vocal o no. El caracter puede estar predefinido o ingresarlo por teclado. Es a libre elección del alumnx ;).


## Ejercicio 2
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

## Ejercicio 3

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

## Ejercicio 4
Escriba un programa que espere un número ingresado `n` por el usuario e imprima en pantalla la suma de los primeros `n números`.
Por ejemplo, si se ingresa el número 5, el programa debe imprimir en pantalla la suma de : `1+2+3+4+5`.

```bash
Ingrese un número: 5

La suma es 15
```

- Hacerlo con iteraciones y teniendo un contador.

- Mejorar el programa y realizar la suma de los primeros n números naturales fórmula matemática $\frac{n(n+1)}{2}$

Pista: Las operaciones entre números soportan paréntesis para dividir términos.


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


# Práctica 7

### Módulos y archivos

Para esta práctica ejercitaremos lo aprendido en las clases de [módulos](https://clases.concristian.com.ar/clase7.html#/2) y [archivos](https://clases.concristian.com.ar/clase8.html#/2).
Para eso, escriba un módulo `files.py` y agregue en el mismo una función por cada ejercicio (Ejercicios del 1 al 10) que será llamado desde el programa principal con la instrucción `import`.
En caso que files.py se ejecute por su cuenta (sin importarlo desde otro archivo), debe imprimir un mensaje de qué es lo que hace el módulo y cada función.

## Ejercicio 1
Escriba una función que permita leer el contenido entero de un archivo de texto y lo imprima en pantalla. Para esto cree un archivo llamado `archivo.txt` desde el bloc de notas o IDE y guardelo en la misma carpeta que el archivo .py de su programa.

## Ejercicio 2
Escriba un programa que lea las primeras `n` filas de un archivo. El número `n` debe ser enviado por el usuario.

## Ejercicio 3
Escriba una función que lea el archivo `mf1.txt` y cuente la cantidad de líneas que arrancan con la letra `M` e imprima la cantidad en pantalla.

Descargar archivo <a href="https://clases.concristian.com.ar/practicas/files/mf1.txt" download="mf1.txt">mf1.txt</a>

## Ejercicio 4
Escriba otra función que permita contar la cantidad de palabras que contiene el archivo del ejercicio anterior.

Pista: Ver uso de [split()](https://www.w3schools.com/python/ref_string_split.asp)

## Ejercicio 5
Escriba una función que permita contar la cantidad de veces que aparece una palabra enviada por el usuario. Por ejemplo:

```bash
Escriba la palabra que desea buscar: Yo
La palabra "Yo" aparece 9 veces
```

## Ejercicio 6
Escriba la función `palabras_cortas()` que lea el archivo `mf1.txt` e imprima las palabras que contienen menos de 4 caracteres.

## Ejercicio 7
Escriba una función que cuente la cantidad de letras mayúsculas que aparece en el archivo `mf1.txt`.

## Ejercicio 8
Escriba una función que permita buscar una palabra dentro del archivo `mf1.txt` y que pueda reemplazarse por otra palabra enviada por el usuario. Se debe guardar en un nuevo archivo llamado `mf1-a.txt`. Utilice las funciones hechas en otros ejercicios, como puede ser el ejercicio 5.

```bash
Escriba la palabra que desea buscar: Yo
La palabra "Yo" aparece 9 veces
Escriba la palabra que desee reemplazar por "Yo": Me
Fue reemplazada la palabra 'Yo' por 'Me' 9 veces.
El resultado se guardó en el archivo 'mf1-a.txt'
```

## Ejercicio 9
Escriba un programa que permita ir agregando contenido a un archivo interactivamente hasta que el usuario escriba `'fin'`.

```bash
Ingrese el texto hasta que llegue una línea con 'fin':

Los hermanos sean unidos porque ésa es la ley primera,
tengan unión verdadera,
en cualquier tiempo que sea,
porque si entre ellos se pelean los devoran los de afuera.
fin

Finalizó la toma de líneas.
```
Ver que el contenido del archivo coincida con lo que ha ingresado por teclado.

## Ejercicio 10
Escriba una función que modifique el contenido del archivo `mf1.txt` para que cada línea empiece con la letra en mayúscula.
Una vez terminado, ejecute nuevamente el ejercicio n y vea como cambia el resultado.

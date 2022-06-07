# Práctica 7

Módulos y archivos

Para esta práctica ejercitaremos lo aprendido en las clases de módulos y archivos.
Para eso, escriba un módulo `files.py` y agregue en el mismo una función por cada ejercicio que será llamado desde el programa principal con la instrucción `import`.
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
La palabra "Yo" aparece 10 veces
```

## Ejercicio 6
Escriba la función `palabras_cortas()` que lea el archivo `mf1.txt` e imprima las palabras que contienen menos de 4 caracteres.

## Ejercicio 7
Escriba una función que cuente la cantidad de letras mayúsculas que aparece en el archivo `mf1.txt`.

## Ejercicio 8
Escriba una función que permita buscar una palabra dentro del archivo `mf1.txt` y que pueda reemplazarse por otra palabra enviada por el usuario. Se debe guardar en un nuevo archivo llamado `mf1-a.txt`

```bash

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

## Ejercicio 11
¿Recuerda el ejercicio 11 de la práctica 4? El del 7 y medio. Agregue la opción que permita guardar el nombre del jugador y las veces que ganó la partida para tener un registro de los mas ganadores.

También agregue una opción para que el programa informe el top 5 de ganadores.

## Ejercicio 12

### Archivos CSV
Los archivos `.csv` (Comma separated values) que significa valores separados por comas, son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de líneas.

Por ejemplo, si queremos representar la siguiente tabla en formato `csv` 

| Marca     | Modelo | Año  | Precio  | Origen |
|-----------|--------|------|---------|--------|
| Ford      | Fiesta | 2013 | 2000.00 | México |
| Chevrolet | Onix   | 2015 | 2190.12 | Brasil |
| Peugeot   | 208 GT | 2019 | 2590.99 | Brasil |

un archivo `CSV` que contiene esa info es el siguiente:

```
Marca,Modelo,Año,Precio,Origen
Ford,Fiesta,2013,2000.00,México
Chevrolet,Onix,2015,2190.12,Brasil
Peugeot,208 GT,2019,2590.99,Brasil
```

Teniendo esto en cuenta, procese el archivo datos.csv y cargue los datos en una lista de diccionarios donde las keys de los diccionarios sean la primer línea del archivo y cada elemento de la lista corresponda a una línea del archivo (excepto la primera).

Si usamos como ejemplo el archivo de arriba, un diccionario posible sería:

```
{
    'Marca': 'Ford',
    'Modelo': 'Fiesta',
    'Año': '2013',
    'Precio': '2000.00',
    'Origen': 'México
}

```






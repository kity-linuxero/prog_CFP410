# Laboratorio 1
> En esta sección de laboratorios veremos algunos ejercicios que puede presentarse en la vida real. Puede usar el buscador en internet para obtener respuestas si no sabe como resolver algo, pero con lo visto en clase es suficiente para resolverlos.


## Ejercicio 1

### Archivos CSV
Los archivos `.csv` (Comma separated values) que significa valores separados por comas, son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de líneas.

Por ejemplo, si queremos representar la siguiente tabla en formato `csv` 

| Marca     | Modelo | Año  | Precio  | Origen |
|-----------|--------|------|---------|--------|
| Ford      | Fiesta | 2013 | 2000.00 | México |
| Chevrolet | Onix   | 2015 | 2190.12 | Brasil |
| Peugeot   | 208 GT | 2019 | 2590.99 | Brasil |

un archivo `csv` que contiene esa info es el siguiente:

```
Marca,Modelo,Año,Precio,Origen
Ford,Fiesta,2013,2000.00,México
Chevrolet,Onix,2015,2190.12,Brasil
Peugeot,208 GT,2019,2590.99,Brasil
```
Observe que se usa la primer línea para definir el nombre de las columnas. Y el resto de líneas contiene los datos.

Teniendo esto en cuenta, desarrolle un programa que procese el archivo <a href="https://clases.concristian.com.ar/labs/data/datos.csv" download="datos.csv">datos.csv</a> y cargue los datos de cada fila en diccionarios donde las keys de los diccionarios sean la primer línea del archivo y cada elemento de la lista corresponda a una línea del archivo (excepto la primera).

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

¿Cómo le parece que puede guardar todas las filas en alguna estructura de datos para consultarlas luego?

Escriba una función que permita buscar por `id` e imprima por pantalla los datos de la fila asociada en el archivo `datos.csv`.


## Ejercicio 2
### Generador de contraseñas

Por nuestra seguridad es muy recomendable utilizar contraseñas fuertes para segurizar nuestras aplicaciones, datos personales y redes sociales. Hoy en día, hasta los navegadores web sugieren contraseñas fuertes y seguras en el momento de registrarnos en alguna plataforma web y el mismo navegador se encarga de guardarla después.
En este ejercicio vamos a desarrollar un generador de contraseñas para ofrecerle al usuario que use nuestro programa contraseñas seguras.

Las contraseñas se componen por caracteres aleatorios que incluyen: caracteres minúsculas, mayúsculas, caracteres especiales y números.

También es necesario preguntarle al usuario la longitud de contraseña que quiere utilizar como también la cantidad de contraseñas a mostrar en pantalla (elija un máximo para no estar generando aleatoriamente infinitas contraseñas).

A continuación se muestra un ejemplo de ejecución:

```
Bienvenido al generador de contraseñas desarrollado por <Su nombre aquí ;)>

Elija la cantidad de caracteres para su contraseña: 8
Elija la cantidad de contraseñas a generar: 5

Sus contraseñas:

dH5T5uhX
Z72EcW+A
%()?$Tb<
2B@UyKd&
k!KKJVTP
```


## Ejercicio 3
### Diccionario de contraseñas

>Importante: cuando hablamos de diccionarios en este ejercicio no nos referimos a las estructuras de datos diccionarios vistas en el curso. Sino, simplemente a una lista de palabras o números.

Un reconocido ISP (proveedor de internet) de Argentina, durante mucho tiempo tuvo como contraseña de WiFi para sus routers, de forma predeterminada un patrón de números seguido del DNI del titular.
Una técnica muy conocida para atacar redes WPA/WPA2 (a día de hoy es el estándar para proteger redes mas utilizado para redes WiFi) es obtener la PSK (la clave) cifrada, que, mediante un __diccionario de datos__  y un algoritmo se pueden ir probando una a una hasta llegar a la clave WiFi en texto plano.

En este ejercicio trataremos de generar el _diccionario de datos_ con los patrones seguidos de números de DNI.

Los patrones que se utilizaban eran: `004`, `011` o `044` seguido por un DNI. Por lo que, si arrancamos a generar nuestro diccionario de datos con el prefijo `004` desde el DNI 20.000.000 hasta el 30.000.000 el archivo de salida generado debe ser de la siguiente forma:

```
00420000000
00420000001
00420000002
00420000003
.
.
.
00429999999
00430000000
```

Como puede ver, simplemente son números generados consecutivamente.

### El programa a desarrollar
Desarrolle un programa que permita generar un _diccionario de datos_ que dé al usuario la opción de elegir el prefijo a usar y luego pregunte desde que número empezar a generar y hasta qué número. Si el usuario no especifica el número se debe empezar por el DNI 00.000.000.
Se muesta a continuación un ejemplo de ejecución

```bash
Bienvenido al generador de diccionario del curso.
Elija el prefijo del diccionario:
1- 004
2- 011
3- 044
Su opción: 1

Elija el número para empezar a generar: 
Elija el número donde termina de generar:
```

En dicho caso no se especificó nada, por lo que empezará de la siguiente manera:

```
00400000000
00400000001
00400000002
.
.
.
00499999998
00499999999
```

Observe que cada línea debe tener 11 caracteres (3 del prefijo y 8 del número de DNI) se deben completar con 0 si es necesario. Para realizar esto, un compañero hizo una búsqueda por internet y encontró que se puede hacer de la siguiente manera: [link](https://www.delftstack.com/howto/python/python-leading-zeros/)

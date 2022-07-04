# Trabajo práctico N1

## Ejercicio 1

### Diccionario de palabras

Hoy en día es muy común que los editores de textos medianamente sofisticados tengan la característica de poder verificar ortografía, palabras y formas de redacción.


Con los conocimientos adquiridos en este curso, estamos en condiciones para poder hacer una coprobación simple de palabras en una cadena de caracteres o archivo y comprobarlos si están en un archivos. Esto le ayudará a reafirmar sus habilidades para programar y resolver problemas.


## Programa a desarrollar

Desarrolle un programa que permita verificar si las palabras escritas en una suceción de palabras se encuentran en un diccionario de palabras en español.


### Primera etapa

Desarrolle un programa que permita que el usuario escriba texto _en modo interactivo_ hasta que llegue la palabra `@fin`. En dicho momento debe terminar la toma de palabras y debe informar la cantidad de palabras escritas que no figuran en el diccionario.


### Segunda etapa
Modifique el programa de la primer etapa para que levante el texto desde un archivo en texto plano.
El programa no debe perder la funcionalidad adquirida en la primer etapa y debe ser capaz de realizar las dos opciones dependiendo la elección del usuario.

### Tercera etapa
Modificar el programa para que reciba parámetros desde el sistema operativo y dependiendo de los parámetros recibidos debe iniciarse en modo interactivo o en modo archivo.

Por ejemplo si su programa se llama `tp1.py` si no recibe ningún parámetro debe iniciarse en modo interactivo.

```
python tp1.py

Iniciado en modo interactivo:

> Escribiendo un texto de prueba para verificar el funcionamiento.
> Debe poder leer varias líneas.
> prueva.
> @fin


El archivo archivo.txt contiene 1 palabra que no se encuentran en el diccionario.
```

Si se envía un parámetro se asume que se está enviando el nombre de un archivo.

```
python tp1.py archivo.txt

Iniciado en modo archivo.

El archivo archivo.txt contiene 1 palabra que no se encuentran en el diccionario.
```
Para realizar esta tercera etapa puede usar uno de los tres métodos mencionados en [este link](https://www.geeksforgeeks.org/command-line-arguments-in-python/).

### Consideraciones
Para mejorar la eficiencia pruebe implementar una `caché` de palabras. El término caché es muy utilizado en la informática para hacer referencia como a una _"ante memoria"_. Puede aprender más acerca de este término [aquí](https://es.wikipedia.org/wiki/Cach%C3%A9_(inform%C3%A1tica)).
El objetivo de esta memoria caché es mejorar el rendimiento de la aplicación. Se presenta la situación que es muy costoso abrir todo el archivo y tenerlo en RAM y a la vez puede haber palabras que se repitan en el trascurso de la búsqueda. Por lo que una forma de aplicar esta memoria es agregar a una estructura de datos las palabras a medida que se vayan buscando en el archivo. Cuando haya que buscar la próxima palabra, antes de abrir el archivo de diccionario a buscarlo es mejor buscarlo en la caché. Y en caso de no encontrarse en la caché debe abrirse en el archivo, comprobar su existencia y copiarla en la estructura caché para volver a consultarla mas adelante.

# Trabajo práctico N°1

## Diccionario de palabras

Hoy en día es muy común que los editores de textos medianamente sofisticados tengan la característica de poder verificar ortografía, palabras y formas de redacción.


Con los conocimientos adquiridos en este curso, estamos en condiciones para poder hacer una comprobación simple de palabras en una cadena de caracteres o archivo y comprobarlos si están bien escritas. Esto le ayudará a reafirmar sus habilidades para programar y resolver problemas.


## Programa a desarrollar

Desarrolle un programa que permita verificar si las palabras escritas en una sucesión de palabras se encuentran en un diccionario provisto de palabras en español.

[Descargar el diccionario](https://www.tlm.unavarra.es/pluginfile.php/12961/mod_resource/content/0/practicas/practica2/spanish.lst)

Tenga en cuenta lo siguiente:
- Para el proceso de las palabras deben pasarse todas a minúsculas.
- Deben eliminarse las tildes. *
- Deben eliminarse las comas, puntos y símbolos especiales.*

* Se proveerá una función para que 

### Primera etapa

Desarrolle un programa que permita que el usuario escriba texto _en modo interactivo_ hasta que llegue la palabra `@fin`. En dicho momento debe terminar la toma de palabras y debe informar la cantidad de palabras escritas que no figuran en el diccionario.

```
¡Bienvenidx al TP1 del curso de programación!
Usted ha ingresado al modo interactivo.

> Hola, estoy probando un texto de prueba. A ver si funciona.
> Texto, texto y mas texto... kljakljdja fasdfas
> @fin

Ha finalizado el ingreso de texto.


El texto contiene 2 palabras que no están en el diccionario.
```


### Segunda etapa
Modifique el programa de la primer etapa para que levante el texto desde un archivo en texto plano.
El programa no debe perder la funcionalidad adquirida en la primer etapa y debe ser capaz de realizar las dos opciones dependiendo la elección del usuario.

### Tercera etapa
Modificar el programa para que reciba parámetros desde el sistema operativo y dependiendo de los parámetros recibidos debe iniciarse en modo interactivo o en modo archivo.

Por ejemplo si su programa se llama `tp1.py` si no recibe ningún parámetro debe iniciarse en modo interactivo.

```
python tp1.py

¡Bienvenidx al TP1 del curso de programación!
Usted ha ingresado al modo interactivo.

> Escribiendo un texto de prueba para verificar el funcionamiento.
> Debe poder leer varias líneas.
> prueva.
> @fin

El texto contiene 1 palabra que no está en el diccionario.
```

Si se envía un parámetro se asume que se está enviando el nombre de un archivo.

```
python tp1.py archivo.txt

Iniciado en modo archivo.

El archivo archivo.txt contiene 1 palabra que no está en el diccionario.
```
Para realizar esta tercera etapa puede usar uno de los tres métodos mencionados en [este link](https://www.geeksforgeeks.org/command-line-arguments-in-python/).

### Cuarta etapa
Modifique el programa para que sea capaz de mostrarle al usuario la palabra que no se encuentra en el diccionario y dé la oportunidad de:
- Re escribir la palabra
- Agregarla al diccionario de palabras
- Ignorar y seguir



```
python tp1.py

¡Bienvenidx al TP1 del curso de programación!
Usted ha ingresado al modo interactivo.

> Escribiendo un texto de prueba para verificar el funcionamiento.
> Debe poder leer varias líneas.
> prueva.
> @fin

La palabra prueva no se encuentra en el diccionario.
¿Qué desea hacer?

1. Agregarla al diccionario
2. Corregir palabra
3. Ignorar y seguir

Su opción: 2
Escriba nuevamente la palabra: prueba

El texto no contiene palabras que no están en el diccionario.
```

### Mejoras posibles (opcional)
Para mejorar la eficiencia pruebe implementar una `caché` de palabras. El término caché es muy utilizado en la informática para hacer referencia como a una _"ante memoria"_. Puede aprender más acerca de este término [aquí](https://es.wikipedia.org/wiki/Cach%C3%A9_(inform%C3%A1tica)).
El objetivo de esta memoria caché es mejorar el rendimiento de la aplicación. Se presenta la situación que es muy costoso abrir todo el archivo y tenerlo en RAM y a la vez puede haber palabras que se repitan en el trascurso de la búsqueda. Por lo que una forma de aplicar esta memoria es agregar a una estructura de datos las palabras a medida que se vayan buscando en el archivo. Cuando haya que buscar la próxima palabra, antes de abrir el archivo de diccionario a buscarlo es mejor buscarlo en la caché. Y en caso de no encontrarse en la caché debe abrirse en el archivo, comprobar su existencia y copiarla en la estructura caché para volver a consultarla mas adelante.

## Forma de entrega

Debe entregarse lo que tenga hasta la semana de las vacaciones de invierno. No hace falta que esté completamente terminadas todas las etapas, pero haga hasta donde pueda.

Enviar un mensaje privado por Slack la URL del repositorio de Github donde subió el trabajo práctico. El repositorio debe tener un archivo readme.md indicando su funcionamiento básico y cuestiones que considere que el instructor deba tener en cuenta para comprender el código y hacerlo funcionar.
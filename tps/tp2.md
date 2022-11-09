# Trabajo práctico N°2

## Taller de GUI

En el Centro de Formación Profesional, todos los años se realiza una muestra en la que cada curso expone material que van realizando a lo largo del año.

La programación tiene su complejidad y lo hemos visto durante el curso, para el resto de personas puede no ser llamativo o entender el código fuente de un programa orientado a objetos siguiendo las mejores prácticas sin embargo, pueden apreciar mas un programa con interface gráfica.

En el curso no hemos visto GUI (Interfaces gráficas de usuario por su siglas en inglés) porque nos enfocamos puramente en programación. Pero también hemos visto el uso de librerías que pueden facilitarnos gran parte del desarrollo, como por ejemplo una interface gráfica.

Existen numerosas librerías para realizar interfaces gráficas para aplicaciones de escritorio (desktop), web, para dispositivos móviles, etc.

Para este taller de GUI proponemos dos alternativas para realizar aplicaciones, pero dejando abierta la oportunidad para que el o la alumna decida cualquier otro:

- Aplicaciones de escritorio utilizando la librería [Tkinter](https://docs.python.org/es/3/library/tkinter.html) 
- Un mini-juego utilizando [arcade](https://api.arcade.academy/en/latest/) o [pygame](https://www.pygame.org/news)


# Ejercicios

Intente realizar los siguientes ejercicios para que algunos de ellos puedan estar en la muestra.

Para ir practicando lo visto con git en las clases anteriores, cree un nuevo repositorio en su cuenta, llamado por ejemplo `tp2-cfp410` donde va a ir subiendo los ejercicios.

Luego, comparta el repositorio con el profesor para que pueda ser evaluado y accesible para el día de la muestra.

Realice los que mas pueda. Le servirá para tener un primer contacto con diseño de GUI simples.

## Saludo por GUI

Desarrolle un programa que tome por un input el nombre de una persona y lo salude.

Pista:
- [Ejercicio resuelto](https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/ejercicios_en_clase/gui/saludo/gui_saludo.py)


## Generador de contraseñas

En el [Lab1](https://github.com/kity-linuxero/prog_CFP410/blob/main/labs/lab1.md#ejercicio-2) hicimos un generador de contraseñas. Puede realizar una GUI para generar contraseñas y mostrarlas en pantalla.

Pista:
- [Ejercicio resuelto](https://github.com/kity-linuxero/prog_CFP410/tree/main/practicas/ejercicios_en_clase/gui/generador_passwd/)


## Descargador de contenido de YouTube
En el Lab3, se vió como usar la librería `pytube` para descargar contenido de Youtube.
En este ejercicio se pide hacer una interface gráfica para realizarlo.

Pista:
- [Ejercicio resuelto](https://github.com/kity-linuxero/prog_CFP410/tree/main/practicas/ejercicios_en_clase/gui/youtube-download/youtube_gui.py)

## Piedra, papel y tijera

Realice una interfaz gráfica para el [ejercicio 10](https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/practica2.md#ejercicio-10) de la práctica 2. Si puede reutilice el código hecho o bien, con los conocimientos posteriores adquiridos reescriba el programa de piedra-papel y tijeras para que quede de forma mas eficiente.

Separe la interfaz gráfica de la lógica del juego en dos módulos por separado.

## Temperatura media de los días de la semana

Desarrolle una interfaz gráfica para el [ejercicio 4](https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/practica4.md#ejercicio-4) de la práctica 4. Donde se recibían las temperaturas medias de cada día de la semana y el programa calculaba qué días se dió la máxima y la mínima.

## Sorteo

Desarrolle una aplicación con gui que permita realizar un sorteo, tipo "rifa" en la que se vayan agregando nombres de personas y cada una elije un número que cuando finalice la toma de números se realice el sorteo y se informe al ganador o ganadora si hubo alguien. Si no hubo nadie, debe dar opción para volver a sortear.

Pistas:
- Puede ayudarse de los  [Listbox](https://recursospython.com/guias-y-manuales/lista-listbox-en-tkinter/) de Tkinter para ir listando a las personas (opcional).
- En la práctica 4, [ejercicio 10](https://recursospython.com/guias-y-manuales/lista-listbox-en-tkinter/) se realizó algo parecido, puede ver su código y modificarlo para adaptarlo.

## Nombres de personas físicas en Argentina

En [datos.gob.ar](datos.gob.ar) se publican datos de relevancia de la República Argentina. Entre esos datos de acceso público, se encuentra la cantidad de personas registradas por nombre y por año.
Por ejemplo, en este [link](https://infra.datos.gob.ar/catalog/otros/dataset/2/distribution/2.21/download/nombres-2015.csv) puede descargarse un _csv_ con los nombres ordenado por la cantidad de gente anotada en el año 2015.

![](./img/names.png)

Por ejemplo, puede verse que el nombre con mayor inscripciones fue _Benjamin_ con 3695, seguido por _Isabella_ con 3294.

Desarrolle un programa que le pida al usuario su nombre y le informe la cantidad de gente anotada con su nombre y en que puesto está su nombre.

Los datos se los puede descargar de [datos.gob.ar](https://datos.gob.ar/dataset/otros-nombres-personas-fisicas). Verá que en algunos archivos los nombres están agrupados en varios años. Elija el que mas le parezca, pero no olvide citar la fuente e informar en alguna parte del programa cual archivo se usó.

Si bien en el pasado hemos usado archivos _csv_ para procesarlos y obtener datos, puede apoyarse de la librería [csv](https://docs.python.org/es/3/library/csv.html) para hacerle mas fácil la extracción de los datos.

# Compilar nuestros programas

El fin de todo programa es ejecutarse en una computadora y muchas veces es deseable ejecutar el programa fuera de nuestro entorno de desarrollo, para que un tercero pueda probar el programa o pueda ser corrido en un ambiente real.

Python es un lenguaje _interpretado_, eso quiere decir que, en vez de compilar su código para ejecutarse, el intérprete se encarga de ejecutar línea por línea el código y el programa así corre en la computadora.
Pero en algún momento vamos a necesitar ejecutar nuestros programas en una computadora que no tenga el intérprete de Python instalado, para eso vamos a necesitar _compilar_ nuestro programa.

Compilar un programa es básicamente, convertir el código fuente a lenguaje de máquina. Una vez compilado el programa no será posible hacer cambios en el código. Si hace falta hacer un cambio hay que volver a compilar el programa.

Es importante destacar que, al momento de compilar un programa debemos tener en cuenta la plataforma y el hardware en la cual vamos a compilar el programa para que luego sea ejecutado. Es decir, el mismo programa que puede correr en una determinada versión de Windows de 64 bits, y no será posible correr en otro sistema operativo como MacOS o GNU/Linux.
Tampoco es el mismo programa compilado el que se ejecurá para una versión de GNU/Linux para una [arquitectura x86_64](https://es.wikipedia.org/wiki/X86-64) y para una GNU/Linux con [arquitectura ARM](https://es.wikipedia.org/wiki/Arquitectura_ARM).

## Compilando nuestros programas

Una forma de compilar nuestros programas escritos en Python es con la librería [pyinstaller](https://pyinstaller.org/en/stable/index.html).

Para instalar la librería:
```bash
pip install -U pyinstaller
```
Compilar nuestro programa
```bash
pyinstaller -F mi_programa.py
```

> El parámetro `-F` se usa para que nuestro programa se empaque en un solo archivo.

Una vez compilado el programa, se generarán dos carpetas:
 - `build`: Se guardarán los archivos temporales durante la compilación
 - `dist`: Es la carpeta que mas nos interesa porque se guardará nuestro programa compilado. Si ejecutamos `pyinstaller` con el parámetro `-F` la carpeta tendrá solo un archivo que será el ejecutable de nuestro programa, de otra manera tendrá una carpeta con muchos archivos que serán necesarios para la ejecución del programa.









#### Documentación adicional:
- [Introducción a Tkinter](https://recursospython.com/guias-y-manuales/introduccion-a-tkinter/)
- [Mas recursos Tkinter](https://recursospython.com/tag/tkinter/)




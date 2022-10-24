# Trabajo práctico N°2

## Taller de GUI

En el Centro de Formación Profesional, todos los años se realiza una muestra en la que cada curso expone material que van realizando a lo largo del año.

La programación tiene su complejidad y lo hemos visto durante el curso, para el resto de personas puede no ser llamativo o entender el código fuente de un programa orientado a objetos siguiendo las mejores prácticas sin embargo, pueden apreciar mas un programa con interface gráfica.

En el curso no hemos visto GUI (Interfaces gráficas de usuario por su siglas en inglés) porque nos enfocamos puramente en programación. Pero también hemos visto el uso de librerías que pueden facilitarnos gran parte del desarrollo, como por ejemplo una interface gráfica.

Existen numerosas librerías para realizar interfaces gráficas para aplicaciones de escritorio (desktop), web, para dispositivos móviles, etc.

Para este taller de GUI proponemos dos alternativas para realizar aplicaciones, pero dejando abierta la oportunidad para que el o la alumna decida cualquier otro:

- Aplicaciones de escritorio utilizando la librería [Tkinter](https://docs.python.org/es/3/library/tkinter.html) 
- Un mini-juego utilizando [arcade](https://api.arcade.academy/en/latest/) o [pygame](https://www.pygame.org/news)

A modo de guía se proponen los siguientes ejercicios para poder aplicar GUI sobre los programas ya realizados a lo largo del curso.

## Ejercicios

### Piedra, papel y tijera

Realice una interfaz gráfica para el [ejercicio 10](https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/practica2.md#ejercicio-10) de la práctica 2. Si puede reutilice el código hecho o bien, con los conocimientos posteriores adquiridos reescriba el programa de piedra-papel y tijeras para que quede de forma mas eficiente.

Separe la interfaz gráfica de la lógica del juego en dos módulos por separado.

### Temperatura media de los días de la semana

Desarrolle una interfaz gráfica para el [ejercicio 4](https://github.com/kity-linuxero/prog_CFP410/blob/main/practicas/practica4.md#ejercicio-4) de la práctica 4. Donde se recibían las temperaturas medias de cada día de la semana y el programa calculaba qué días se dió la máxima y la mínima.

### Sorteo

Desarrolle una aplicación con gui que permita realizar un sorteo, tipo "rifa" en la que se vayan agregando nombres de personas y cada una elije un número que cuando finalice la toma de números se realice el sorteo y se informe al ganador o ganadora si hubo alguien. Si no hubo nadie, debe dar opción para volver a sortear.

Pistas:
- Puede ayudarse de los  [Listbox](https://recursospython.com/guias-y-manuales/lista-listbox-en-tkinter/) de Tkinter para ir listando a las personas (opcional).
- En la práctica 4, [ejercicio 10](https://recursospython.com/guias-y-manuales/lista-listbox-en-tkinter/) se realizó algo parecido, puede ver su código y modificarlo para adaptarlo.
















Por ejemplo, estas son algunas ideas:

- Interfaz gráfica para el generador de contraseñas realizado en el [Lab1](https://github.com/kity-linuxero/prog_CFP410/blob/main/labs/lab1.md#ejercicio-2)
- Una interfaz gráfica para la calculadora de edad [Lab2](https://github.com/kity-linuxero/prog_CFP410/blob/main/labs/lab2.md#calculadora-de-edad)
- Una interfaz gráfica para el descargador de videos de YouTube visto en el [Lab3](https://github.com/kity-linuxero/prog_CFP410/blob/main/labs/lab3.md#descargar-contenido-de-youtube)

- Una interfaz gráfica para el juego realizado de piedra-papel-tijera
- Juego de [plataforma](https://api.arcade.academy/en/latest/examples/index.html#platformers) (estilo Mario Bross)
- Juego de [naves](https://api.arcade.academy/en/latest/examples/index.html#shooting-with-sprites) (estilo Space Invaders)


Documentación adicional:
- [Introducción a Tkinter](https://recursospython.com/guias-y-manuales/introduccion-a-tkinter/)
- [Mas recursos Tkinter](https://recursospython.com/tag/tkinter/)
- [Documentación Arcade](https://api.arcade.academy/en/latest/get_started.html)
- [Cómo hacer un juego con PYGAME en 10 minutos](https://openwebinars.net/blog/como-hacer-un-juego-con-pygame-en-10-minutos/)


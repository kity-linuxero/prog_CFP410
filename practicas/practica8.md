# Práctica 8 - Programación orientada a Objetos - Parte I

En esta práctica nos concentraremos en consolidar los temas vistos en teorías, **clases**, **objetos**, **métodos** y **atributos** que son los conceptos básicos de la programación orientada a objetos.

## Ejercicio 1
Desarrolle un programa que modele el comportamiento de un auto que posea: Una patente, marca, modelo y un kilometraje. El auto debe ser capaz de realizar recorridos en kilómetros a una velocidad. Por ejemplo debe entender el mensaje, `recorrido(velocidad, kilometros)`. A medida que el auto realiza los recorridos, el kilometraje va a ir aumentando (el kilometraje empieza en 0 en el momento de creación del objeto). También, el auto debe entender el mensaje `kilometraje()` que imprima en pantalla el kilometraje actual.

## Ejercicio 2
Modifique el programa anterior para que el auto avise cada 10.000km que es necesario realizar el mantenimiento preventivo. El auto debe entender el mensaje `realizar_mantenimiento()` . En el momento que se realiza el mantenimiento no debe volver avisar sobre el mantenimiento hasta los próximos 10.000kms.

## Ejercicio 3
Realice un programa que procese a personas que van a ir ingresando en una sala. La personas deben ser modeladas en una clase `Persona` que contenga los datos nombre y edad. Además un objeto persona debe ser capaz de poder presentarse mediante el mensaje `presentarse()` donde dirá `"Hola, soy {nombre} y tengo {edad} años"`.

Para cargar los nombres de persona, pida al usuario que ingrese nombre y edad de personas hasta que llegue la persona `@fin`. Las personas deben guardarse en una lista y al finalizar la carga de datos deben presentarse todas las personas.

## Ejercicio 4
Escriba un programa que modele el comportamiento de una TV como se describe a continuación: Un TV tiene dos estados, `encendido` y `apagado`, además tiene la información del canal actual (un número entre 2 y 135) y el volumen del audio (un número entre 0 a 10). El TV debe entender los mensajes:
- `encender`: Enciende el TV y cambia el estado a encendido.
- `apagar`: Apaga el TV y cambia el estado a apagado.
- `canal_up()`: Cambia al canal siguiente hacia arriba.
- `canal_down()`: Cambia al canal siguiente hacia arriba.
- `cambiar_a_canal(n_canal)`: Cambia el canal actual al canal pasado por parámetro.
- `volumen_up()`: Incrementa el volumen.
- `volumen_down()`: Decrementa el volumen.


Escriba los atributos y métodos que considere necesario. También tenga en cuenta qué pasa cuando se quiere cambiar de canal cuando el TV está apagado, o encender cuando ya está encendido.

## Ejercicio 5
>_En este ejercicio se verá que es posible tener un objeto definido anteriormente como atributo de otro objeto_.

Modifique el programa del punto anterior para que sea posible asignarle un _control remoto_.

El control remoto será otra clase `ControlRemoto` que entenderá los siguientes mensajes:
- `asignar(un_TV)`: Asigna un TV para controlar.
- `encender`: Enciende el TV.
- `apagar`: Apaga el TV.
- `canal_up()`: Cambia al canal siguiente hacia arriba.
- `canal_down()`: Cambia al canal siguiente hacia arriba.
- `cambiar_a_canal(n_canal)`: Cambia el canal actual al canal pasado por parámetro.
- `volumen_up()`: Incrementa el volumen.
- `volumen_down()`: Decrementa el volumen.

De esa manera, el control remoto tiene como atributo un TV. Tenga en cuenta que los _métodos_ para cambiar de canal ya están implementados en el TV, por lo que el _Control remoto_ solo debe ordenarle al TV que haga lo que pide.





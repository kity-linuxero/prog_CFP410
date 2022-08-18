# Práctica 8 - Programación orientada a Objetos - Parte I

En esta práctica nos concentraremos en consolidar los temas vistos en teorías, **clases**, **objetos**, **métodos** y **atributos** que son los conceptos básicos de la programación orientada a objetos.

## Ejercicio 1
Desarrolle un programa que modele el comportamiento de un auto. El auto posee una marca, modelo y un kilometraje. El auto debe ser capaz de realizar recorridos en kilómetros a una velocidad. Por ejemplo debe entender el mensaje, `recorrido(velocidad, kilometros)`. A medida que el auto realiza los recorridos, el kilometraje va a ir aumentando (el kilometraje empieza en 0 en el momento de creación del objeto). También, el auto debe entender el mensaje `kilometraje()` que imprima en pantalla el kilometraje actual.

## Ejercicio 2
Modifique el programa anterior para que el auto avise cada 10.000km que es necesario realizar el mantenimiento preventivo. Y debe imprimir el mensaje `Es necesario realizar el mantenimiento preventivo` antes de cada recorrido cuando hayan pasado la cantidad de kilómetros para realizar el mantenimiento.. El auto debe entender el mensaje `realizar_mantenimiento()`. En el momento que se realiza el mantenimiento no debe volver avisar sobre el mantenimiento hasta los próximos 10.000kms.

## Ejercicio 3
Realice un programa que procese a personas que van a ir ingresando en una sala. La personas deben ser modeladas en una clase `Persona` que contenga los datos nombre y edad. Además un objeto persona debe ser capaz de poder presentarse mediante el mensaje `presentarse()` donde dirá `"Hola, soy {nombre} y tengo {edad} años"`.

Para cargar los nombres de persona, pida al usuario que ingrese nombre y edad de personas hasta que llegue la persona `@fin`. Las personas deben guardarse en una lista y al finalizar la carga de datos deben presentarse todas las personas.

## Ejercicio 4
Implemente con _POO_ una _Pila_. La Pila consiste en una estructura de datos como las que vinimos usando como _Listas_ pero en este caso usaremos nuestra propia estructura con los propios mensajes y se comporta como una estructura _LIFO_ (Last In-Fist Out) es decir, el último elemento en ingresar es el primero en salir. La Pila deberá ser _genérica_ en cuanto a que puede guardar cualquier tipo de datos.

Para eso, nuestra Pila debe entender los mensajes:
- `apilar(elemento)`: Apila un elemento. Lo agrega en la estructura.
- `desapilar()`: Retorna el elemento de "más arriba" y lo quita de la pila.
- `top()`: Retorna el elemento de mas arriba pero no lo quita de la pila.
- `vacia()`: Retorna si la pila está vacía (`True`/`False`)
- `cant_elementos()`: Retorna _la cantidad_ de elementos que hay en la pila.


## Ejercicio 5
Modifique su solución para el [ejercicio en clase](https://clases.concristian.com.ar/clasePoo.html#/ejercicio) de POO de la siguiente manera:

Modele con POO el comportamiento de unos encendedores.

Los encendedores deben poder encenderse y apagarse según el combustible disponible y además deben poseer un número de fabricación. Dicho número se establece en el momento que de instancien los objetos _Encendedor_ y deben ser números consecutivos. Por ejemplo, el primer encendedor instanciado será el número de serie 1, el siguiente el 2 y así sucesivamente. Para hacer esto, tenga en cuenta algún mecanismo para que _la clase_ lleve la cuenta del número de fabricación para asignar a sus instancias.

Los encendedores deben tener los siguientes metodos:
- `encender()`: Enciende el encendedor si hay combustible disponible.
- `apagar()`: Apaga el encendedor.
- `recargar_combustible()`: Recarga el tanque de butano al 100%.
- `num_serie()`: Informa el número de serie del encendedor.

Los encendedores además constan de un tanque de butano con una capacidad máxima de 10 encendidos. Cada vez que se enciende el encendedor, la capacidad disminuye en uno. Si el tanque está vacío no será posible encenderlo (`No hay suficiente combustible`).

El tanque de butano debe tener _sus propios_ atributos y métodos. Para eso defina la clase **Tanque_de_butano** con los siguientes métodos.
- `recargar()`: Completa la capacidad de carga al 100%
- `esta_vacio()`: Retorna si está vació
- `consumir_encendido()`: Consume la capacidad necesaria para un encendido. Cada encendido resta 1 en la carga del tanque.
- `cantidad_de_combustible()`: Imprime en pantalla el % que resta en el tanque, por ejemplo: `Resta un 80% de la carga`.

Definir la clase Encendedor con los atributos y métodos que considere necesarios para modelarlo como se pide. Recuerde que el tanque de butano debe ser una _instancia_ de la clase **Tanque_de_butano**.

Escribir un programa que cree un encendedor, lo encienda 11 veces y una vez agotado el tanque, lo recargue y lo encienda una vez mas.

## Ejercicio 6
Escriba un programa que modele el comportamiento de una TV como se describe a continuación: Un TV tiene dos estados, _encendido_ y _apagado_, además tiene la información del _canal actual_ (un número entre 2 y 135) y el _volumen_ del audio (un número entre 0 a 10).

El TV debe entender los mensajes:
- `encender`: Enciende el TV y cambia el estado a encendido.
- `apagar`: Apaga el TV y cambia el estado a apagado.
- `canal_up()`: Cambia al canal siguiente hacia arriba.
- `canal_down()`: Cambia al canal siguiente hacia arriba.
- `cambiar_a_canal(n_canal)`: Cambia el canal actual al canal pasado por parámetro.
- `canal_actual()`: Retorna el canal actual
- `volumen_up()`: Incrementa el volumen.
- `volumen_down()`: Decrementa el volumen.
- `volumen_actual()`: Retorna el volumen actual
- `cambiar_a_volumen(n_volumen)`: Cambia el volumen a un valor pasado por parámetro. (Tenga en cuenta las limitaciones del mismo) `0<=volumen<=10`.


Escriba los atributos y métodos que considere necesario. También tenga en cuenta qué pasa cuando se quiere cambiar de canal cuando el TV está apagado, o encender cuando ya está encendido.
A tener en cuenta:
- Cuando llega al canal 135 y se pide un `canal_up()` debe volver al canal 2.
- Cuando el volumen llega a 10 y se pide un `volumen_up()` debe mantenerse en 10.
- Trate de _reutilizar los métodos_. Si se fija, algunos métodos pueden lograr su objetivo interactuando con otros métodos ya implementados.

Algunos métodos van a necesitar que impriman por pantalla lo que hacen. A continuación se deja un ejemplo de ejecución:
```bash
# Se enciende el TV
TV encendido en canal 4
# Se cambia un canal hacia arriba
Canal: 5
# Se cambia un canal hacia arriba
Canal: 6
# Se sube el volumen
Volumen: 1
# Se apaga el TV
TV apagado
```

## Ejercicio 7

Modifique el programa del punto anterior para que sea posible controlar el TV con un _control remoto_.

El control remoto será otra clase, `ControlRemoto` que entenderá los siguientes mensajes:
- `asignar(un_TV)`: Asigna un TV para controlar. El TV es enviado por parámetro.
- `encender`: Enciende el TV.
- `apagar`: Apaga el TV.
- `canal_up()`: Cambia al canal siguiente hacia arriba.
- `canal_down()`: Cambia al canal siguiente hacia arriba.
- `cambiar_a_canal(n_canal)`: Cambia el canal actual al canal pasado por parámetro.
- `volumen_up()`: Incrementa el volumen.
- `volumen_down()`: Decrementa el volumen.
- `canal_previo()`: Cambia al canal previo.
- `mute()`: Quita el audio (volumen a 0)
- `info_canal()`: Imprime `"Estás viendo el canal {n}"`

Tenga en cuenta que los _métodos_ para interactuar con el televisor ya están implementados en la clase TV por el ejercicio anterior.




# Práctica 5

En esta práctica aplicaremos temas vistos a modo de repaso y veremos métodos y funciones útiles que nos servirán en la vida real programando.

## Procesamiento de strings y listas


### Introducción

Los strings pueden ser tratados como listas o arrays. Esto es así en muchos lenguajes. Por ejemplo, podemos tener el siguiente código:

```python
# Acceder a una letra en particular. Podemos verla como la posición en un array
nombre = "Cristian"
print (nombre[0])
```
#### Output:
```bash
C
```
#### Iterar en un string

```python
nombre = "Cristian"

for l in nombre:
    print (l)
```

#### Output:
```bash
C
r
i
s
t
i
a
n
```

También tenemos varios métodos para usar en strings. Algunos los vimos en las clases, otros puede consultarlos en [este link]("https://ellibrodepython.com/cadenas-python").

Teniendo eso en cuenta,

## Parte práctica


## Ejercicio 1

Escribir una función que imprima cada caracter de un string enviado por parámetro.
La cadena debe ser enviada por teclado desde el programa principal.

## Ejercicio 2

Escribir una función que pida un string y luego un caracter y cuente la cantidad de veces que aparece un caracter en una cadena. El valor debe retornarlo como resultado de la función y ser impreso desde el programa.

## Ejercicio 3

Escriba una función que retorne la cantidad de palabras que contiene una cadena. Por ejemplo:
```
"Hola a todos" # 3
"Hola" # 1
"Nos invitaron a un lugar que tenía buena pinta pero al final resultó ser súper random" # 16
```

## Ejercicio 4

Escriba un programa que reciba una cantidad de nombres de personas. Luego los imprima pero con la primer letra en mayúsculas y el resto en minúscula.

Por ejemplo:

```bash
Ingrese un nombre: cristian
Ingrese un nombre: DAVID
Ingrese un nombre: aNTOneLla
Ingrese un nombre: .

Las personas son:
Cristian
David
Antonella

```

### Ejercicio 5

Escriba una función que retorne (por True o False) si una subcadena está incluída en una cadena.
Por ejemplo:

```bash
estaEn(Ana, Amanda) # False
estaEn(Ana, Ananda) # True
```

### Ejercicio 6

Escriba una función que valide una _dirección de e-mail_ (retorne True o False según el caso). La dirección de e-mail se compone de `<nombre>@<sub-dominio>.<dominio>.<dominio2>...`

- `programacion@concristian.com.ar` será un e-mail válido.
- `programacion@@concristian.com.ar` NO será un e-mail válido.
- `programacion@concristian` NO será un e-mail válido.
- `clases.concristian.com.ar` NO será un e-mail válido.
- `clases.concristian.com.` NO será un e-mail válido.









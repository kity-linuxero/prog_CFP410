# Práctica 6

Práctica sobre diccionarios y tuplas


## Ejercicio 1

Escribir un programa que guarde en una variable el siguiente diccionario `{'Dolar':'$', 'Euro':'€', 'Yen':'¥', 'Peso argentino':'$'}` y pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. En tal caso se termina el programa.

```bash
Ingrese una divisa para saber el símbolo: Euro
El símbolo es: €
Ingrese una divisa para saber el símbolo: hola
La divisa no existe.
Fin del programa
```

## Ejercicio 2

Modifique el diccionario anterior para que agregue el valor de la divisa respecto al peso argentino. Y luego pida al usuario que ingrese un monto en pesos argentinos para calcular el equivalente a una divisa deseada en ambos sentidos.

```bash
Ingrese monto en pesos: 800
Ingrese la divisa para convertir: Euro

800 pesos argentinos es equivalente a: 6,30 €
1€ es igual a 127.07 pesos argentinos

```

## Ejercicio 3

Se tiene el siguiente diccionario:
`{ 'Mayonesa':'140,50', 'Cerveza': 130, 'Agua mineral': 110.15, Servilleta: 65.20 }`.
Escriba un programa que permita simular una compra donde se van ingresando productos y cantidad. Los valores se van sumando para tener el total para cobrar al finalizar la compra.
La compra termina cuando el usuario ingresa `fin` donde se deberá finalizar la compra e informar el monto total.
También debe ser posible saber el parcial de una compra cuando se ingresa `parcial` donde deberá informar el monto gastado hasta el momento pero sin finalizar la compra:
A continuación se muestra un ejemplo de ejecucición del programa:

```bash
Ingrese producto: Mayonesa
Ingrese cantidad: 3
El precio es: $421.50
----------------------
Ingrese producto: Cerveza
Ingrese cantidad: 2
El precio es: $260
----------------------
Ingrese producto: parcial
Parcial compra: $681,50
----------------------
Ingrese producto: computadora
El producto no existe
----------------------
Ingrese producto: Servilleta
Ingrese cantidad: 1
El precio es: $65.20
----------------------
Ingrese producto: fin
----------------------
El total de su compra es: $ 746,70
```

## Ejercicio 4
Se tiene el siguiente diccionario:
```python
diccionario = {
    "clase": {
        "estudiante": {
            "nombre": "Mike",
            "materias": {
                "matematica": 7,
                "geografia": 8
            }
        }
    }
}
```

Desarrolle un programa para que imprima la nota de geografía.

## Ejercicio 5

### Parte práctica

Escriba una función llamada `tupla(n)` que cree una tupla de `n` elementos. La cantidad es enviada por parámetro. Se debe retornar dicha tupla.

### Unit-test
Un `unit-test` o "prueba unitaria" es una forma de comprobar que el código funcione correctamente. Muchas veces se prueba una función enviandole una entrada conocida esperando una salida esperada. Si la función en su valor de retorno coincide con el valor esperado se dice que el test pasa (OK o pass).

En el ejercicio citado probaremos si una función hace realmente lo que necesitamos pasando un test. Para eso, ingrese en el [link]("https://www.mycompiler.io/view/HmQb6r2sS3q") y clickee en el botón __Fork__ para poder modificar el código. Luego copie y pegue su función en el lugar indicado:

```python
#### INICIO FUNCION A DESARROLLAR

# MODIFIQUE ESTA FUNCION PARA QUE PASE EL TEST
'''
    Esta función debe crear una tupla con n elementos
'''
def tupla(n):
    print (n)
    
#### FIN FUNCION A DESARROLLAR
```

Ejecute el programa con el botón __Run__. La salida debe ser la siguiente:

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

[Execution complete with exit code 0]
```

Más adelante profundizaremos en Unit-tests pero como puede ver es una herramienta muy potente para probar nuestro código.

## Ejercicio 6









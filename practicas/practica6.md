# Práctica 6

Práctica sobre diccionarios


## Ejercicio 1

Escribir un programa que guarde en una variable el diccionario `{'Dolar':'$', 'Euro':'€', 'Yen':'¥', 'Peso uruguayo':'$'}` y pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. En tal caso se termina el programa.

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

Escribir un programa que guarde en un diccionario los precios de unos productos (por unidad) y luego, a pedido del usuario imprima el precio por tantas unidades.
Por ejemplo, se tiene el diccionario: 
`{ 'Mayonesa':'140,50', 'Cerveza': 130, 'Agua mineral': 110.15, Servilleta: 65.20 }`.
Se simula una compra donde se van ingresando productos y cantidad. Los valores se van sumando para tener el total para cobrar al finalizar la compra.
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
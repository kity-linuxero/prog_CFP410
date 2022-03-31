# Practica 1 - Ejercicio 10
# Escribir un programa que simule ser un cajero automático donde se extrae dinero de la cuenta. 
# El programa debe consultar al usuario la cantidad que desea extraer.
# Si el dinero que desea extraer es menor al saldo total, la extracción será exitosa y deberá informar el monto extraído y el saldo restante. 
# Si se solicita un monto que excede el monto, el programa deberá decir saldo insuficiente.

# Esta versión del programa mejora en caso que el usuario ingrese una letra o un número negativo.
dinero= 900
extraccion = input("Ingrese el monto que desea extraer:")

# Mientras no sea un valor numérico válido, volverá a pedir el dato. 
# isnumeric() devolverá false
while not extraccion.isnumeric():
    extraccion = input("Ingrese el monto valido para extraer:")

# Se convierte a número
extraccion = int(extraccion)

if extraccion <= dinero:
    dinero = dinero - extraccion
    print (f"Usted ha extraído ${extraccion}")
else:
    print("No hay suficiente saldo para completar la operación")

print  (f"El saldo restante es: ${dinero}")
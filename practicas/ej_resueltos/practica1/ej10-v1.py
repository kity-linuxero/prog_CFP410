dinero= 900
extraccion = int(input("Ingrese el monto que desea extraer:"))

if extraccion <= dinero:
    dinero = dinero - extraccion
    print (f"Usted ha extraído ${extraccion}")
else:
    print("No hay suficiente saldo para completar la operación")

print  (f"El saldo restante es: ${dinero}")
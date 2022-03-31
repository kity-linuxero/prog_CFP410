dinero= 900
extraccion = int(input("Ingrese el monto que desea extraer:"))

if extraccion <= dinero:
    dinero = dinero - extraccion
    print ("Usted ha extraído $" + str(extraccion))
else:
    print("No hay suficiente saldo para completar la operación")

print  ("El saldo restante es: $" + str(dinero))
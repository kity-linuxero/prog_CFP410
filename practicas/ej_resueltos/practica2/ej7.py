n1= int(input("Ingrese la nota en el primer examen"))
n2= int(input("Ingrese la nota en el segundo examen"))
n3= int(input("Ingrese la nota en el tercer examen"))

# Para descartar que no haya una menor a 6. En ese caso no promociona
mayor_6 = ((n1 >= 6) and (n2 >= 6) and (n3 >= 6))

# El promedio
prom = (n1+n2+n3)/3

if mayor_6 and prom >= 8:
    print("Resultado: ¡La o el alumno promocionó la materia! :D")
else:
    print("Resultado: La o el alumno NO promocionó la materia :(")
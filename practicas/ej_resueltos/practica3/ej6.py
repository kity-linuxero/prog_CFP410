# EJERCICIO HECHO EN CLASE 12/04/22
def menor(n1,n2):
    if n1 < n2:
        return n1
    else:
        return n2
        
def mayor(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

# Programa principal

# Ingresar un número por teclado
n = int(input("Ingrese un número: "))
# tener un máximo
min, max = n, n
# tener un mínimo

while n >=0:
    max = mayor(n, max)
    min = menor(n, min)
    n = int(input("Ingrese un número: "))
    
print (f"El mayor es {max} y el menor es {min}")
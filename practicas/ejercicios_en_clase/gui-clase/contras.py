'''
Desarrollado por Ivan
'''
def generador_contraseñas(cantidad):
    import string
    import random
    from random import choice
    alfamin=string.ascii_lowercase
    alfamay=string.ascii_uppercase
    numeros=string.digits
    especiales=string.punctuation
    bolsa=alfamin+alfamay+numeros+especiales

    contra=""
    
    for b in range(int(cantidad)):
        c=choice(bolsa)
        contra += c

    return(contra)

if __name__ == '__main__':
    cant = int(input("Ingrese la cantidad de caracteres: "))
    print (generador_contraseñas(cant))
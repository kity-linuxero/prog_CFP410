# Escriba un programa que le pida al usuario que ingrese un número del 1 al 6 y simule la función que se lanza un dado...
# El programa debe seguir hasta que el usuario acerte el número.

import random

# ######## VARIABLES GLOBALES ######## 
acierte = False

######## SECCIÓN FUNCIONES/MODULOS ########

# Retorna True o False según si miNumero es igual a dado. 
def acerte(miNumero, dado):
    return miNumero == dado

# Retorna un valor entre 1 y 6 que simula ser el lanzamiento de un dado.
def tirarDado():
    return random.randint(1, 6)

# Pide un número al usuario.
def pedirNumero():
    miNum = int(input("Ingrese un número del dado: "))
    while (miNum >= 6 or miNum <= 0):
        miNum = int(input("Ingrese un número Válido (1 al 6): "))
    return miNum

######## PROGRAMA PRINCIPAL ########

while not acierte:
    miJugada = pedirNumero()
    dado = tirarDado()
    acierte = acerte(miJugada, dado)
    print (f"Salió el número {dado}")
   
print("Finalizó el juego")
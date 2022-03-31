# Ejercicio 10 - Practica 2
# Escriba un juego para jugar piedra, papel o tijera

import random

# Constantes
PIEDRA=1
PAPEL=2
TIJERA=3

# LA PC elije su opción antes de pedirnos
pc = random.randint(1, 3)

# El usuario ingresa su opción
user=input("Elija una opción:\n1) Piedra\n2) Papel\n3) Tijera.")

#Opcional es para descartar datos inválidos por si ingresa una letra o cualquier cosa.
while not user.isnumeric() or not (1 <= int(user) <= 3):
    print("Opción inválida")
    user=input("Elija una opción:\n1) Piedra\n2) Papel\n3) Tijera.")
    
# Convierto a número la elección del usuario para poder compararlo
user = int(user)

userGano = ((pc==PIEDRA and user==PAPEL) or (pc==PAPEL and user == TIJERA) or (pc==TIJERA and user==PIEDRA))

pc_op = pc
if pc_op==PIEDRA:
    pc_op="PIEDRA"
elif pc_op==PAPEL:
    pc_op="PAPEL"
else:
    pc_op="TIJERA"

if userGano:
    print(f"¡Ganaste!, yo elegí {pc_op} :(")
elif pc==user:
    print(f"¡Empatamos! yo también elegí {pc_op} :P")
else:
    print(f"¡Perdiste!, yo elegí {pc_op} XD")

    
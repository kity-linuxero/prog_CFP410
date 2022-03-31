# Ejercicio 10 - Practica 2
# Escriba un juego para jugar piedra, papel o tijera.
# A diferencia del ejercicio 10, este pregunta si queremos jugar otra vez y totaliza las victorias y derrotas que tuvimos

import random

# Constantes
PIEDRA=1
PAPEL=2
TIJERA=3

# Cuenta las victorias y derrotas
wins=0
lost=0

# Para seguir jugando
seguirJugando = True

while seguirJugando:

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
        wins+=1
    elif pc==user:
        print(f"¡Empatamos! yo también elegí {pc_op} :P")
    else:
        print(f"¡Perdiste!, yo elegí {pc_op} XD")
        lost+=1

    jugar=input("¿Querés jugar otra vez? (S/n): ")

    #Opcional es para descartar datos inválidos por si ingresa una letra o cualquier cosa.
    seguirJugando = (jugar!='n')

# Se usa un short if para saber si tiene que decir en plural o singular la cantidad de victorias/derrotas.
#
print(f"¡Terminó el juego!.\nVos ganaste {wins} {'vez' if wins == 1 else 'veces'}.\nYo gané {lost} {'vez' if lost == 1 else 'veces'}.")

# Se usa un short if para imprimir un emoji al final. Si la máquina perdió se mostrará triste
# Por esa razón, mostrará un :(
print(f"{'XD' if lost > wins else ':(' if lost < wins else ':P'}")




    
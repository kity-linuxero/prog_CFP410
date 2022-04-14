# Escriba un juego para jugar piedra, papel o tijera.
# Este programa pregunta si queremos jugar otra vez y totaliza las victorias y derrotas que tuvimos
# Se usa modularización extrema XD

import random

# Constantes. Se usan para hacer mas legible el código. Es opcional.
PIEDRA=1
PAPEL=2
TIJERA=3

# Variables GLOBALES que cuentan las victorias y derrotas
wins=0
lost=0

# Me devuelve true si el usuario ganó, false en caso contrario
def userGano(pc, user):
    # Aquí puede verse la utilidad de las constantes usadas arriba, de otra manera estaríamos comparando números.
    return ((pc==PIEDRA and user==PAPEL) or (pc==PAPEL and user == TIJERA) or (pc==TIJERA and user==PIEDRA))

# Devuelve True si hubo empate, False en caso contrario
def hubo_empate(pc,user):
    return pc==user

# Ingresa un número y lo devuelve en texto para poder decir que opción eligió la computadora
def opcion_a_texto(opcion):
    if opcion==PIEDRA:
        return "PIEDRA"
    elif opcion==PAPEL:
        return "PAPEL"
    else:
        return "TIJERA"

# El usuario ingresa su opción. Descarta valores inválidos. Devuelvo un número (int)
def elige_usuario():
    user=input("Elija una opción:\n1) Piedra\n2) Papel\n3) Tijera\nSu opción: ")

    while not user.isnumeric() or not (1 <= int(user) <= 3):
        print("Opción inválida")
        user=input("Elija una opción:\n1) Piedra\n2) Papel\n3) Tijera\nSu opción: ")
    # Convierto a número la elección del usuario para poder compararlo
    return int(user)

# La PC elige su opción
def elige_pc():
    return random.randint(1, 3)

# Se usa para imprimir el resumen final de victorias y derrotas
def informar_resumen():
    # Se usa un short if para saber si tiene que decir en plural o singular la cantidad de victorias/derrotas.
    print(f"¡Terminó el juego!.\nVos ganaste {wins} {'vez' if wins == 1 else 'veces'}.\nYo gané {lost} {'vez' if lost == 1 else 'veces'}.")
    # Se usa un short if para imprimir un emoji al final. Si la máquina perdió se mostrará triste
    # Por esa razón, mostrará un :(
    print(f"{'XD' if lost > wins else ':(' if lost < wins else ':P'}")

# Devuelve True si el usuario quiere jugar otra vez.
# True si apreta cualquier tecla distinta a 'n'. False si llega 'n'
def quiere_jugar_otra_vez():
    jugar=input("¿Querés jugar otra vez? (S/n): ")
    return (jugar!='n')

def informar_gano_usuario(opcion_pc):
    print(f"¡Ganaste!, yo elegí {opcion_a_texto(opcion_pc)} :(")

def informar_empate(opcion_pc):
    print(f"¡Empatamos! yo también elegí {opcion_a_texto(opcion_pc)} :P")

def informar_gano_pc(opcion_pc):
    print(f"¡Perdiste!, yo elegí {opcion_a_texto(opcion_pc)} XD")


############################################################
################## Programa principal ######################
############################################################


# Para seguir jugando
seguirJugando = True

# Trampa On/Off ;)
con_trampa = False

while seguirJugando:

    # LA PC elije su opción antes de pedirnos
    eleccion_pc = elige_pc()
          
    eleccion_user = elige_usuario()

    # Almacena en gano por True o False si el usuario ganó
    usuario_gano_partida = userGano(eleccion_pc,eleccion_user) 

    # Ejercicio  9 donde se aplica la trampa. Si no está activada (con_trampa=False) se ignora la línea donde la pc tira nuevamente.
    if con_trampa and usuario_gano_partida:
        # PC tira otra vez
        eleccion_pc = elige_pc()

    if usuario_gano_partida:
        # Gano usuario
        informar_gano_usuario(eleccion_pc)
        wins+=1
    elif hubo_empate(eleccion_pc,eleccion_user):
        # Hubo empate
        informar_empate(eleccion_pc)
    else: # Ganó la PC
        informar_gano_pc(eleccion_pc)
        lost+=1

    seguirJugando = quiere_jugar_otra_vez()

informar_resumen()


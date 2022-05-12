# Ejercicio hecho en clase por todos
import random

# Crear mazo
def crear_mazo():
    mazo= []
    for c in range(1,13):
        for p in range(4):
            if not (c==8 or c==9):
                mazo.append(c)
    return mazo

def sacar_carta(un_mazo):
    carta= random.choice(un_mazo)
    un_mazo.remove(carta)
    return carta

def valor_carta(una_carta):
    if una_carta <= 7:
        return una_carta
    else:
        return 0.5

def game_over(un_puntaje):
    #return (un_puntaje > 7.5)
    if un_puntaje > 7.5:
        return True
    else:
        return False

def cant_jugadores():
    a = input("Ingrese la cantidad de jugadores: ")
    while not (a.isnumeric()) or int(a) <2:
        a = input("Ingrese la cantidad de jugadores: ")
    return int(a)

def preguntar_seguir_jugando():
    opcion = input("¿Quiere seguir jugando? (s/n): ")
    while opcion != 's' and opcion != 'n':
        opcion = input("¿Quiere seguir jugando? (s/n): ")
    if opcion == 's':
        return True
    else:
        return False

mazo = crear_mazo() 

jugadores = cant_jugadores()
puntos_mayor = 0
jugador_ganador = 0
# Programa principal

for j in range(1, jugadores+1):
    puntos_j = 0
    sigue_jugando = True

    print(f"-- Turno del jugador {j} --")
    input("Enter para continuar\n")
    
    while not game_over(puntos_j) and sigue_jugando:
        carta = sacar_carta(mazo)
        puntos_j += valor_carta(carta)

        print(f"Su carta es: {carta}\nSu puntaje es {puntos_j}")

        if game_over(puntos_j):
            print("PERDISTE!")
        else:
            sigue_jugando = preguntar_seguir_jugando()

    print(f"Terminó el jugador {j}. Su puntaje es: {puntos_j}\n")

    if puntos_mayor < puntos_j and not game_over(puntos_j):
        puntos_mayor = puntos_j
        jugador_ganador = j

print(f"El ganador fue el jugador {jugador_ganador} con {puntos_mayor} puntos.")
    
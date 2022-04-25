import random

# Crea un mazo de carta y lo retorna
def crear_mazo():
    mazo=[]
    for c in range(12):
        # El segundo for es para crear 4 cartas de cada número (uno por palo)
        for c2 in range(4):
            # El if es para descartar los 8 y 9.
            if not 8 <= c+1 <= 9:
                mazo.append(c+1)
    return mazo

# Baraja (mezcla) un mazo enviado por parámetro
def barajar_mazo(unMazo):
    random.shuffle(unMazo)

# Retorna el valor de una carta Los valores válidos son 1 al 7 y 10, 11 y 12.
def puntos_carta(unaCarta):
    if unaCarta <= 7:
        return unaCarta
    else:
        return 0.5

# Saca la primer carta del mazo y la retorna como parámetro
def sacar_carta(unMazo):
    return unMazo.pop(0)

# Retorna por sí o no si un jugador perdió.
def game_over(unPuntaje):
    return (unPuntaje > 7.5)

# Consulta al usuario la cantidad de jugadores y lo retorna al programa
def numero_de_jugadores():
    n_jugadores = int(input("Ingrese la cantidad de jugadores que van a participar (mínimo 2): "))
    while n_jugadores < 2:
        n_jugadores = int(input("Ingrese la cantidad de jugadores que van a participar (mínimo 2): "))
    return n_jugadores


def informar_carta(una_carta):
    print(f"Su carta es: {una_carta}")

# Pregunta si el usuario quiere otra carta. Por defecto será que sí.
def otra_carta():
    carta = input("¿Desea sacar otra carta? (S/n): ")
    return carta != 'n'

# Realiza el informe en pantalla de la jugada
def informar_puntaje_jugador(unJugador, elPuntaje):
    print (f"Jugador #{unJugador+1}. Terminó su turno. \nSu puntaje es: {elPuntaje}")

# Hará una búsqueda de máximo. En caso de empate gana el que primero jugó
def buscar_ganador(lista_de_puntajes):
    max = 0
    winer = 0

    for l in lista_de_puntajes:
        if l > max and l < 7.5:
            winer = lista_de_puntajes.index(l)
            max= l

    print (f"\n¡Ganó el jugador {winer+1} con {max} puntos!")
             

mazo = crear_mazo()
barajar_mazo(mazo)

print("¡Bienvenido al juego de 7 y medio del curso de Programación!")

n_jugadores = numero_de_jugadores()

# Variable para guardar el puntaje de los jugadores
puntajes = []

for i in range(n_jugadores):

    puntaje_actual = 0.0
    otra_carta_mas = True
    print (f"\n-- Turno jugador #{i+1} --")

    while not game_over(puntaje_actual) and otra_carta_mas : # Mientras no se pase del puntaje
        mi_carta_actual = sacar_carta(mazo)
        informar_carta(mi_carta_actual)

        puntaje_actual += puntos_carta(mi_carta_actual) # Suma los puntajes con la nueva carta
        print(f"Lleva {puntaje_actual} puntos.")
        if not game_over(puntaje_actual):
            otra_carta_mas = otra_carta()

    informar_puntaje_jugador(i, puntaje_actual)
    puntajes.append(puntaje_actual)

buscar_ganador(puntajes)

    









# print(mazo)

# print (sacar_carta(mazo))
# print (sacar_carta(mazo))
# print (sacar_carta(mazo))
# print (sacar_carta(mazo))
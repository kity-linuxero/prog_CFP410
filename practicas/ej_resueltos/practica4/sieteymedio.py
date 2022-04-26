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

def numero_de_jugadores():
    """
    Consulta al usuario la cantidad de jugadores y lo retorna al programa.
    No es necesaria tantos ifs y demás cosas vistas en este módulo. Pero se hace para mostrar que el input
    si lo modularizamos lo podemos hacer tan potente como queramos.
    
    """
    n_jugadores = input("\nIngrese la cantidad de jugadores que van a participar (mínimo 2 - Por defecto 2): ")

    # Por si no ha ingresado nada se toma el valor por defecto.
    if n_jugadores == '':
        return 2
    
    n_jugadores = int(n_jugadores)
    while n_jugadores < 2:
        n_jugadores = int(input("Ingrese la cantidad de jugadores que van a participar (mínimo 2): "))
    return n_jugadores

def informar_carta(una_carta, puntaje_actual):
    print(f"Su carta es: {una_carta}")
    print(f"Lleva {puntaje_actual} puntos.") # Informa 

def otra_carta():
    """
    Pregunta si el usuario quiere otra carta. Por defecto será que sí.
    Retorna False si el input es una n caso contrario True
    """
    carta = input("¿Desea sacar otra carta? (S/n): ")
    return carta != 'n'

def informar_puntaje_jugador(unJugador, elPuntaje):
    """
    Realiza el informe en pantalla de la jugada

    """
    # Se informa unJugador+1 porque recuerden que el índice de una lista arranca en 0.
    print (f"Jugador #{unJugador+1}. Terminó su turno.")
    if elPuntaje <= 7.5: # Si se pasó no se informa el puntaje.
        print(f"Su puntaje es: {elPuntaje}")

    print ("------------------------")


# Hará una búsqueda del puntaje máximo. En caso de empate gana el que primero jugó
def buscar_ganador(lista_de_puntajes):
    max = 0
    winer = 0
    for l in lista_de_puntajes:
        if l > max and l <= 7.5:
            winer = lista_de_puntajes.index(l) # Guarda el índice de la lista donde se almacenó el puntaje del jugador
            max= l # Se almacena el puntaje para informarlo después.

    # Se informa winer+1 porque el índice de la lista empieza en 0.
    # El jugador #1 se guarda en la primer posición de la lista, es decir en la 0. 
    # Por esa razón hay que informar el +1. Para que no informe le jugador # 0 y sea mas legible.
    if max != 0:
        print (f"\n¡Ganó el jugador {winer+1} con {max} puntos!\n")
    else:
        print ("¡NO HUBO GANADORES!\n")
    print ("Gracias por haber jugado a este maravilloso juego :) \n")
             

## EMPIEZA EL PROGRAMA PRINCIPAL ##

mazo = crear_mazo() # mazo será la lista que contendrá las cartas.
barajar_mazo(mazo) # "Mezcla" las cartas para alterar el orden.

print(" ¡Bienvenido al juego de 7 y medio del curso de Programación! ".center(70,'*'))

n_jugadores = numero_de_jugadores()

# Variable para guardar el puntaje de los jugadores. Arranca con una lista vacía
puntajes = []

# Cada iteración será el turno de un jugador.
for i in range(n_jugadores):

    input(f"\nTurno jugador #{i+1}.\nPresione una tecla para continuar.\n")

    puntaje_actual = 0 # El puntaje se arranca de 0
    otra_carta_mas = True # Se pone en true para que sea capaz de pedirle la primer carta.
    # print (f"\n-- Turno jugador #{i+1} --") # Como el índice de la lista arranca en 0. Se informa i+1

    while not game_over(puntaje_actual) and otra_carta_mas : # Mientras no se pase del puntaje
        mi_carta_actual = sacar_carta(mazo) # Es la carta actual

        puntaje_actual += puntos_carta(mi_carta_actual) # Suma los puntajes con la nueva carta

        informar_carta(mi_carta_actual, puntaje_actual) # La imprime en pantalla junto con el total de los puntos

        # Este if se hace para que, en el caso que se pase no vuelva a pedir una carta
        if not game_over(puntaje_actual):
            otra_carta_mas = otra_carta() # Le pregunta al usuario si desea otra carta mas o se planta
        else:
            print("¡Perdiste!")

      

    informar_puntaje_jugador(i, puntaje_actual) # Informa el puntaje del turno del jugador.
    puntajes.append(puntaje_actual) # Almacena el puntaje. 

    # print (f"\n-- Terminó turno jugador #{i+1} --") # Como el índice de la lista arranca en 0. Se informa i+1

buscar_ganador(puntajes)

    









# print(mazo)

# print (sacar_carta(mazo))
# print (sacar_carta(mazo))
# print (sacar_carta(mazo))
# print (sacar_carta(mazo))
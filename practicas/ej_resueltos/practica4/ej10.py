"""
Escriba un programa que reciba la apuesta de n jugadores. A los jugadores se les pregunta el nombre y el número al cual apuestan. 
Las apuestas son números entre 0 y 99 y puede ser que varios jugadores apuesten al mismo número. 
Una vez que todos los jugadores hayan realizado su apuesta, el programa sortea un número entre 0 y 99. 
Puede ser que no haya ganadores, o haya mas de uno. Debe informar si hay ganadores o no y debe decir el nombre de los ganadores.
"""

def apuesta_valida(un_numero):
    return 0 <= un_numero <= 99

def registrar_apuesta(lista_de_apuestas):
    nombre = input(f"\nIngrese su nombre: ")
    
    apuesta = int(input(f"Ingrese su apuesta: \n-----------\n"))
    apuesta = []
    apuesta.append(nombre)
    apuesta.append(apuesta)
    lista_de_apuestas.append(apuesta)



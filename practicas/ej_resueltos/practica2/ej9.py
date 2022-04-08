import random

acerto = False

while not acerto:
    miNum = int(input("Ingrese un número del dado: "))
    num = random.randint(1, 6)
    print (f"Salió el número {num}")
    acerto = miNum == num

print("Finalizó el juego")

    

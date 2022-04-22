
def crear_mazo():
    mazo=[]
    for c in range(12):
        # El segundo for es para crear 4 cartas de cada número (uno por palo)
        for c2 in range(4):
            # El if es para descartar los 8 y 9.
            if not 8 <= c+1 <= 9:
                mazo.append(c+1)
    return mazo


crear_mazo()
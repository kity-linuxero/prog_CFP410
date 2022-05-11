semana = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
temps = []

for d in semana:
    
    a = input (f"Ingrese temperatura media en el día {d}: ")
    while not a.isnumeric():
        a = input (f"Ingrese temperatura media en el día {d}: ")
    a = float(a)
    temps.append(a)

maxd = ''
mind = ''
maxt = 0
mint = 99999999

for t in temps:
    if t > maxt:
        maxt = t
        maxd = semana[temps.index(t)]
    else:
        if t < mint:
            mint = t
            mind = semana[temps.index(t)]
    
print (f"La máxima se dió el día {maxd}, con {maxt}ºC")
print (f"La mínima se dió el día {mind}, con {mint}ºC")


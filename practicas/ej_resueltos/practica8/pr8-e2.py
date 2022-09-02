"""
Modifique el programa anterior para que el auto avise cada 10.000km que es necesario realizar el mantenimiento preventivo.
Y debe imprimir el mensaje Es necesario realizar el mantenimiento preventivo antes de cada recorrido cuando hayan pasado la cantidad de kilómetros 
para realizar el mantenimiento.. El auto debe entender el mensaje realizar_mantenimiento(). 
En el momento que se realiza el mantenimiento no debe volver avisar sobre el mantenimiento hasta los próximos 10.000kms.
"""

class Auto:
    KM_PARA_MANTENIMIENTO = 10000

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ultimo_mantenimiento = 0
        self.km = 0

    def mantenimiento_necesario(self):
        return ((self.km - self.ultimo_mantenimiento) > Auto.KM_PARA_MANTENIMIENTO)

    def realizar_mantenimiento(self):
        self.ultimo_mantenimiento = self.km

    def recorrer(self, velocidad, kilometros):
        if self.mantenimiento_necesario():
            print("¡Es necesario realizar el mantenimiento!")
        self.km = self.km + kilometros
        print (f"Recorriendo {kilometros}kms a {velocidad}km/h")
        
    def kilometraje(self):
        print(f"Kilometraje: {self.km}")

    

a = Auto('Ford', 'Fiesta')
a.recorrer(200, 20001)
a.realizar_mantenimiento()
a.recorrer(120, 15000)
a.recorrer(120, 15000)
print(a.ultimo_mantenimiento)
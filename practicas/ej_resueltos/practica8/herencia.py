class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas
        
class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindrada):
        super().__init__(color, 4)
        self._velocidad = velocidad
        self._cilindrada = cilindrada
        
class Camioneta(Coche):
    def __init__(self, color, velocidad, cilindrada, carga):
        super().__init__(color, 4, velocidad, cilindrada)
        self._carga = carga
        
class Bicicleta(Vehiculo):
    def __init__(self, color, tipo):
        super().__init__(color, 2)
        self._tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, tipo, velocidad, cilindrada):
        super().__init__(color,tipo)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    def __str__(self):
        return(f"Tipo: {type(self).__name__}\nColor:{self._color}\nTipo:{self._tipo}\nVelocidad:{self._velocidad}\nCilindrada: {self._cilindrada}")

       
#c = Camioneta('Rojo', 4, 180, 2300, 2500)

m = Motocicleta('Blanco', 'Urbana', 120, 150)

print(m)
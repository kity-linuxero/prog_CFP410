class Vehiculo:
    def __init__(self, max_tanque, consumo_km_lts, precio_combustible):
        self._tanque_combustible = 0
        self.km = 0
        self.max_tanque = max

    def cargar_combustible(self):
        pass

    def recorrido(self, km):
        pass

    def autonomia(self):
        pass

    def cantidad_combustible(self):
        pass

    def llenar_tanque(self):
        pass
    
    def kilo(self):
        return self.km

    

class Auto(Vehiculo):
    MAX_TANQUE = 51
    CONSUMO_KM_LTS=6.13
    PRECIO_COMBUSTIBLE=172.3


        
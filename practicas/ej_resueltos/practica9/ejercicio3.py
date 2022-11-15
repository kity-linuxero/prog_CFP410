from random import choice

class Cuenta_bancaria:
    INTERES=0.009
    def __init__(self, titular):
        self.__saldo= 0.0
        self.__titular=titular

    def saldo_disponible(self):
        return self.__saldo

    
    def depositar (self, un_monto):
        self.__saldo+=un_monto
        return True
    def _extraer (self, un_monto):
        self.__saldo-=un_monto
    def __con_interes (self, un_monto):
        return un_monto-(un_monto*Cuenta_bancaria.INTERES)
    def transferir (self, cuenta_bancaria, un_monto):
        self._extraer(un_monto)
        cuenta_bancaria.depositar(self.__con_interes(un_monto))
    def modificar_limite_extraccion (self, un_monto, un_limite):
        if un_monto > un_limite and self._autorización_de_limite()==False:
            return False
        else:
            un_limite=un_monto
            return True
    def titular (self):
        return self.__titular
    def modificar_titular (self, nombre):
        self.__titular=nombre
    def _autorización_de_limite (self):
        return choice([True, False])
    def __str__(self):
        return f"Titular de cuenta: {self.titular()}\nMonto en la cuenta: ${self.saldo_disponible()}"

class Caja_ahorro (Cuenta_bancaria):
    
    def __init__(self, titular):
        super().__init__(titular)
        self.__limite_extraccion= 30000

    def extraer(self, un_monto):
        if self.saldo_disponible()>=un_monto and un_monto < self.__limite_extraccion:
            super()._extraer(un_monto)
            return True
        else:
            print("Limite de extraccion excedido")
            return False

    def modificar_limite_extraccion (self, un_monto):
        super().modificar_limite_extraccion(un_monto, self.__limite_extraccion)

    def get_limite_extraccion(self):
        return self.__limite_extraccion
        


class Cuenta_corriente (Cuenta_bancaria):

    def __init__(self, titular):
        super().__init__(titular)
        self.__limite_extraccion= 50000
        self.__descubierto= 10000
    
    def modificar_limite_descubierto (self, un_monto):
        if un_monto > self.__descubierto and self._autorización_de_limite()==False:
                print("Nuevo límite descubierto: Rechazado")
                return False
        else:
            self.__descubierto=un_monto
            print("Nuevo límite descubierto: Aceptado")
            return True
    
    def limite_descubierto (self):
        return self.__descubierto

    def extraer(self, un_monto):
        if un_monto < self.__limite_extraccion and (self.saldo_disponible()-un_monto) > (self.limite_descubierto()*-1):
            super()._extraer(un_monto)
            return True
        else:
            print("No es posible realizar la operación.")
            return False


    def modificar_limite_extraccion (self, un_monto):
        super().modificar_limite_extraccion(un_monto, self.__limite_extraccion)

    """
    def modificar_limite_extraccion (self, un_monto):
        if un_monto > self.__limite_extraccion and self._autorización_de_limite()==False:
            print("Extensión de límite Rechazado.")
        else:
            self.__limite_extraccion=un_monto
            print(f"Nuevo límite Aceptado.\n\tLímite: {self.__limite_extraccion}")
    """

if __name__ == '__main__':
    cliente1= Cuenta_corriente("Ivan")
    cliente1.depositar(10000)
    print(cliente1.saldo_disponible())
    cliente1.extraer(8000)
    print(cliente1.saldo_disponible())
    cliente1.extraer(7000)
    print(cliente1.saldo_disponible())
    cliente1.modificar_limite_descubierto(15000)
    cliente1.extraer(9000)
    print(cliente1.saldo_disponible())
    print(cliente1.titular())
    cliente1.extraer(17000)
    print(cliente1.saldo_disponible())
    print(cliente1)
    cliente1.depositar(300000)
    cliente1.modificar_limite_extraccion(200000)
    cliente1.extraer(180000)
    print(cliente1.saldo_disponible())
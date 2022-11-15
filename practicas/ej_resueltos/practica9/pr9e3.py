import random

class Cuenta_bancaria():

    COMISION_POR_TRANSFERENCIA = 0.991
    
    def __init__(self, titular, limite_extraccion):
        self.__saldo = 0
        self._set_limite_extraccion(limite_extraccion)
        self.modificar_titular(titular)

    def modificar_titular(self, un_titular):
        self.__titular = un_titular

    def _set_limite_extraccion(self, limite_extraccion):
        self.__limite_extraccion = limite_extraccion
        return True

    def get_limite_extraccion(self):
        return self.__limite_extraccion

    def titular(self):
        return self.__titular

    def saldo_disponible(self):
        return self.__saldo

    def depositar(self, un_monto):
        if un_monto > 0:
            self.__saldo += un_monto
            return True

    def _extraer(self, un_monto):
        if un_monto >= 0:
            self.__saldo -= un_monto
            return True
        else:
            return False

    def transferir(self, cuenta_destino, un_monto):
        if un_monto <= self.saldo_disponible():
            self._extraer(un_monto)
            cuenta_destino.depositar(un_monto*Cuenta_bancaria.COMISION_POR_TRANSFERENCIA)

    def modificar_limite_extraccion(self, un_monto):
        if un_monto < self.get_limite_extraccion() or self._autorizacion():
            return self._set_limite_extraccion(un_monto)
        else:
            return False

    def _autorizacion(self):
        return random.choice([True, False])

    def __str__(self):
        return f"-------------\nTitular: {self.titular()}\nTipo cuenta: {type(self).__name__}\nSaldo: ${self.saldo_disponible()}\nLimite extraccion: ${self.get_limite_extraccion()}"



class Caja_ahorro(Cuenta_bancaria):

    LIMITE_EXTRACCION_DEFAULT = 30000
    
    def __init__(self, titular):
        super().__init__(titular, Caja_ahorro.LIMITE_EXTRACCION_DEFAULT)

    def extraer(self, un_monto):
        if un_monto <= self.get_limite_extraccion() and un_monto <= self.saldo_disponible():
            return super()._extraer(un_monto)
        else:
            return False


class Cuenta_corriente(Cuenta_bancaria):

    LIMITE_EXTRACCION_DEFAULT = 50000
    DESCUBIERTO_DEFAULT = 10000

    def __init__(self,titular):
        super().__init__(titular, Caja_ahorro.LIMITE_EXTRACCION_DEFAULT)
        self.__set_descubierto(Cuenta_corriente.DESCUBIERTO_DEFAULT)

    def __set_descubierto(self, un_monto):
        self.__descubierto = un_monto
        return True

    def limite_descubierto(self):
        return self.__descubierto

    def modificar_limite_descubierto(self, un_monto):
        if un_monto < self.limite_descubierto() or self._autorizacion():
            return self.__set_descubierto(un_monto)
        else:
            return False

    def extraer(self, un_monto):
        if un_monto <= self.get_limite_extraccion() and un_monto <= (self.saldo_disponible() + self.limite_descubierto()):
            return super()._extraer(un_monto)
        else:
            return False

    def __str__(self):
        return f"{super().__str__()}\nLimite descubierto: ${self.limite_descubierto()}"
        
    def transferir(self, cuenta_destino, un_monto):
        if un_monto <= self.saldo_disponible()+self.limite_descubierto():
            super()._extraer(un_monto)
            cuenta_destino.depositar(un_monto*Cuenta_bancaria.COMISION_POR_TRANSFERENCIA)

if __name__ == '__main__':
    
    ca = Caja_ahorro('Laura')
    ca.extraer(100)

    print(ca)

    #cc.depositar(101)
    #ca.depositar(299)
    # print(cc)
    # cc.transferir(ca,101)
        
    # print(ca)
    # print(cc)

        

    

    





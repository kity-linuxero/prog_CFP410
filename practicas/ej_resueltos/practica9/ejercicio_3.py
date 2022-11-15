import random

class Cuenta_bancaria:
	COMISION_TRANSFERENCIA = .9

	def __init__(self, titular):	
		self.__titular = titular
		self.__saldo = 0
		print(f'''Se ha abierto una {type(self).__name__}\nTitular: {self.__titular}\nSaldo: ${self.saldo()}\n''')

	def mostrar_saldo(self):
		print(f'Saldo: {self.saldo():.2f}')

	def saldo(self):
		return self.__saldo

	def depositar(self, un_monto):
		self.__saldo+= un_monto
		return True

	def extraccion(self, un_monto):
		self.__saldo-= un_monto		

	def transferencia(self, cuenta_bancaria, un_monto):
		self.extraccion(un_monto)
		cuenta_bancaria.depositar(un_monto*(1 - Cuenta_bancaria.COMISION_TRANSFERENCIA/100))
		return True
		

	def modificar_limite_extracción(self, limite_extraccion):
		self.__limite_extraccion = limite_extraccion
		print(f'Su nuevo límite de extracción es: {limite_extraccion}')
		return True

	def titular(self):
		print(f'Titular: {self.__titular}' )
		return self.__titular

	def modificar_titular(self, nombre):
		self.__titular = nombre 	

	def decidir(self):
		return random.choice([True,False])

class Caja_ahorro(Cuenta_bancaria):
	LIMITE_EXTRACCION = 30000
	LIMITE_DESCUBIERTO = 0

	def __init__(self,titular):
		super().__init__(titular)
		self.__limite_extraccion = Caja_ahorro.LIMITE_EXTRACCION
		self.__limite_descubierto = Caja_ahorro.LIMITE_DESCUBIERTO
		
	def extraer(self, un_monto):
		if un_monto <= self.__limite_extraccion:
			self.extraccion(un_monto)
			print(f'Extracción: {un_monto}, Saldo: {self.saldo():.2f}')
			return True
		else:
			print('Ha excedido el monto de extracción diario permitido')
			return False

	def transferir(self, cuenta_bancaria, un_monto):
		if un_monto <= self.saldo():
			self.transferencia(cuenta_bancaria,un_monto)
			print(f'Transferencia ${un_monto}, Saldo: ${self.saldo():.2f}')
			return True
		else:
			print('No es posible transferir ese monto')
			return False

	def deposito(self, un_monto):
		self.depositar(un_monto)
		print(f'Depósito: ${un_monto}, Saldo: ${self.saldo():.2f}')
		return True

class Cuenta_corriente(Cuenta_bancaria):
	LIMITE_EXTRACCION = 50000
	LIMITE_DESCUBIERTO = 10000

	def __init__(self,titular):
		super().__init__(titular)
		self.__limite_descubierto = Cuenta_corriente.LIMITE_DESCUBIERTO
		self.__limite_extraccion = Cuenta_corriente.LIMITE_EXTRACCION
		
	def modificar_limite_descubierto(self,limite_descubierto):
		if limite_descubierto < self.__limite_descubierto:
			self.__limite_descubierto = limite_descubierto
			print(f'Su nuevo limite para operar en escubierto es: {limite_descubierto}')
			return True
		else:
			opcion = self.decidir()
			if opcion:
				self.__limite_descubierto = limite_descubierto
				print(f'Su nuevo limite para operar en escubierto es: {limite_descubierto}')
				return True
			else: 
				print('Se ha denegado el cambio de limite para operar en dscubierto.')
				return False

	def transferir(self, cuenta_bancaria, un_monto):
		if un_monto <= ( self.__limite_descubierto + self.saldo()):
			self.transferencia(cuenta_bancaria,un_monto)
			print(f'Transferencia ${un_monto}, Saldo: ${self.saldo():.2f}')
			return True
		else:
			print('No es posible transferir ese monto')
			return False

	def extraer(self, un_monto):
		if un_monto <= self.__limite_extraccion:
			if un_monto <= ( self.__limite_descubierto + self.saldo()):
				self.extraccion(un_monto)
				print(f'Extracción: ${un_monto}, saldo: ${self.saldo():.2f}')
				return True
		print('Ha excedido el monto de extracción diario permitido')
		return False

	def deposito(self, un_monto):
		self.depositar(un_monto)
		print(f'Depósito: ${un_monto}, Saldo: ${self.saldo():.2f}')




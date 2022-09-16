'''
Ejercicio 2 de la práctica 9.
Implementación de Estructura de datos, Pilas y Colas 
'''

class Estructura_de_datos:

    def __init__(self):
        self.__data = []

    def _get_data(self):
        return self.__data

    def cant_elementos(self):
        return len(self._get_data())

    def vacia(self):
        return self._get_data()==[]

    def _agregar_elemento(self, elem):
        self._get_data().append(elem)

    def _quitar_elemento(self, index):
        return self._get_data().pop(index)

    def _top(self, index):
        if not self.vacia():
            return self._get_data()[index]


class Pila(Estructura_de_datos):
    
    def apilar(self, elemento):
        super()._agregar_elemento(elemento)

    def top(self):
        return super()._top(-1)

    def desapilar(self):
        return super()._quitar_elemento(-1)

    
class Cola(Estructura_de_datos):
    
    def encolar(self, elemento):
        super()._agregar_elemento(elemento)

    def top(self):
        return super()._top(0)

    def desencolar(self):
        return super()._quitar_elemento(0)

    
import unittest

from estructura_datos import *


class TestPila(unittest.TestCase):
    def test_pila_crear(self):
        """
        Test para verificar si se crea un objeto de la clase Pila
        """
        p = Pila()
        
        self.assertIsInstance(p, Pila, msg="Se espera una instancia de Pila")

        
    def test_pila_vacia(self):
        """
        Test para verificar si el método vacia() funciona correctamente
        """
        p = Pila()
        self.assertTrue(p.vacia(), msg="Se espera True en una lista vacía")
        p.apilar(33)
        self.assertFalse(p.vacia(), msg="Se espera False en una lista NO vacía")

    def test_pila_cant_elementos(self):
        """
        Test para verificar si el método cant_elementos() funciona correctamente
        """
        p= Pila()
        self.assertEqual(0, p.cant_elementos(), msg="Una Pila vacía debe tener 0 elementos")
        p.apilar(99)
        p.apilar(88)
        p.apilar(77)
        self.assertEqual(3, p.cant_elementos(), msg="Se esperan 3 elementos")
        p.apilar(33)
        self.assertEqual(4, p.cant_elementos(), msg="Se esperan 4 elementos")
        

    def test_pila_desapilar(self):
        """
        Test para verificar el método desapilar()
        """
        p= Pila()
        p.apilar(99)
        p.apilar(88)
        p.apilar(77)

        self.assertEqual(77,p.desapilar(), msg="Se espera otro valor")
        self.assertEqual(88,p.desapilar(), msg="Se espera otro valor")
        self.assertEqual(99,p.desapilar(), msg="Se espera otro valor")

    def test_pila_top(self):
        """
        Test para verificar el método top() de Pila
        """
        p= Pila()
        p.apilar(99)
        p.apilar(88)
        p.apilar(77)

        self.assertEqual(77,p.top(), msg="Se el valor 77")


class TestCola(unittest.TestCase):
    def test_cola_crear(self):
        """
        Test para verificar si se crea un objeto de la clase Cola
        """
        p = Cola()
        
        self.assertIsInstance(p, Cola, msg="Se espera una instancia de Cola")

    def test_cola_vacia(self):
        """
        Test para verificar el método vacia() de Cola
        """
        c = Cola()
        self.assertTrue(c.vacia(), msg="Se espera True en una lista vacía")
        c.encolar(33)
        self.assertFalse(c.vacia(), msg="Se espera False en una lista NO vacía")

    def test_cola_cant_elementos(self):
        """
        Test para verificar el método cant_elementos() de Cola
        """
        c = Cola()
        self.assertEqual(0, c.cant_elementos(), msg="Se esperan 0 elementos para una cola vacía")
        c.encolar(99)
        c.encolar(88)
        c.encolar(77)
        self.assertEqual(3, c.cant_elementos(), msg="Se esperan 3 elementos")
        c.encolar(33)
        self.assertEqual(4, c.cant_elementos(), msg="Se esperan 3 elementos")
        
    def test_cola_desencolar(self):
        """
        Test para verificar el método desencolar()
        """
        c = Cola()
        c.encolar(99)
        c.encolar(88)
        c.encolar(77)

        self.assertEqual(99,c.desencolar(), msg="Se espera otro valor")
        self.assertEqual(88,c.desencolar(), msg="Se espera otro valor")
        self.assertEqual(77,c.desencolar(), msg="Se espera otro valor")
        

    def test_cola_top(self):
        """
        Test para verificar el método top() de cola
        """
        c = Cola()
        c.encolar(99)
        c.encolar(88)
        c.encolar(77)

        self.assertEqual(99,c.top(), msg="Se espera el valor 99")     

if __name__ == '__main__':
    unittest.main()

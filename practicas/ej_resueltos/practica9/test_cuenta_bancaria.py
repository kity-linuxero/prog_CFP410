import unittest

from ejercicio_3 import *


class TestCuentaAhorro(unittest.TestCase):

    def create_ca(self):
        ti = 'Sergio Pérez'
        ca = Caja_ahorro(ti)
        return ca

    def test_crear_ca(self):
        
        
        ca = self.create_ca()

        self.assertIsInstance(ca,Caja_ahorro)
        self.assertEqual(0,ca.saldo_disponible(), msg="El saldo debería ser 0")
        self.assertEqual('Sergio Pérez',ca.titular())

    def test_depositar_ca(self):
        
        ca = self.create_ca()

        self.assertTrue(ca.depositar(1000), msg="Se espera un True si el deposito fue correcto")
        self.assertEqual(1000, ca.saldo_disponible(), msg="Tendría que haber 1000")
        self.assertTrue(ca.depositar(100), msg="Se espera un True si el deposito fue correcto")
        self.assertEqual(1100, ca.saldo_disponible(),  msg="Tendría que haber 1100")
    
    def test_extraccion_ca(self):

        ca = self.create_ca()
        self.assertFalse(ca.extraer(100), msg="Debería ser False")
        self.assertEqual(0, ca.saldo_disponible(), msg="Debería ser 0")

        ca.depositar(1000)
        self.assertTrue(ca.extraer(500))
        self.assertEqual(500,ca.saldo_disponible())

    def test_limite_extraccion_ca(self):
        ca = self.create_ca()
        ca.depositar(50000)
        self.assertFalse(ca.extraer(30001), msg="Supera el límite de extracción")
        self.assertEqual(50000,ca.saldo_disponible(), msg="Se le descontó")

    def test_modificar_titular_ca(self):
        ca = self.create_ca()
        ca.modificar_titular('Carlos Sainz')
        self.assertEqual('Carlos Sainz', ca.titular())

    def test_modificar_limite_extraccion_ca(self):
        ca = self.create_ca()
        ca.modificar_limite_extraccion(2000)
        self.assertEqual(2000, ca.get_limite_extraccion())

    
    def test_transferencia_fallida_ca(self):
        ca = self.create_ca()
        ca2 = self.create_ca()

        ca.depositar(10000)

        ca.transferir(ca2, 4000000000)

        self.assertEqual(10000,ca.saldo_disponible())
        self.assertEqual(0,ca2.saldo_disponible())

    def test_transferencia_correcta_ca(self):
        ca = self.create_ca()
        ca2 = self.create_ca()

        ca.depositar(10000)

        ca.transferir(ca2, 10000)

        self.assertEqual(10000*0.991,ca2.saldo_disponible())
        self.assertEqual(0,ca.saldo_disponible())

    







    




        



        


if __name__ == '__main__':
    unittest.main()
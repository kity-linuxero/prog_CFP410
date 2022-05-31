import unittest
from random import randrange


#### INICIO FUNCION A DESARROLLAR

# MODIFIQUE ESTA FUNCION PARA QUE PASE EL TEST
'''
    Esta función debe crear una tupla con n elementos
'''
def tupla(n):
    print (n)
    
#### FIN FUNCION A DESARROLLAR



# UNIT-TEST
class TestCFP(unittest.TestCase):
    
    def test_tupla_long(self):
        self.assertEqual(19,len(tupla(19)))
        
    def test_tupla_tipo(self):
        self.assertTrue(type(tupla(2)) is tuple)

if __name__ == '__main__':
    unittest.main()
    

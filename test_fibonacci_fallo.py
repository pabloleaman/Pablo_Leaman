# Se importa modulo "unittest" que permite crear tests unitarios.
import unittest

# Se importa el modulo que contiene la serie de Fibonacci, la cual se quiere testear.
import Fib_prueba

# Se crea la clase que contendran los respectivos tests.
class TestFibonacci(unittest.TestCase):

    # Se define test para probar funcion que retorna la posicion n de la serie de Fibonacci
    def test_numero(self):
        self.assertNotEqual(Fib_prueba.Fib(6), 8)  # Retorna fallo si F_6 == 8
        
    # Se define test para probar funcion que retorna la posicion n-1 de la serie de Fibonacci
    def test_anterior(self):
        self.assertEqual(Fib_prueba.Fib_anterior(8),13) # Retorna fallo si F_7 != 13
        

    
# Se ejecutan los respectivos tests de forma automatica al compilar.
if __name__ == '__main__':
    unittest.main()

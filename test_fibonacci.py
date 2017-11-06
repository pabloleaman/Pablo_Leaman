# Se importa modulo "unittest" que permite crear tests unitarios.
import unittest

# Se importa el modulo que contiene la serie de Fibonacci, la cual se quiere testear.
import Fib_prueba

# Se crea la clase que contendran los respectivos tests.
class TestFibonacci(unittest.TestCase):

    # Se define test para probar funcion que retorna la posicion n de la serie de Fibonacci
    def test_numero(self):
        self.assertEqual(Fib_prueba.Fib(7), 13) # Retorna error si F_7 != 13

    # Se define test para probar funcion que retorna la posicion n-1 de la serie de Fibonacci
    def test_anterior(self):
        self.assertEqual(Fib_prueba.Fib_anterior(10),34) # Retorna error si F_10 != 34
        

    
# Se ejecutan los respectivos tests de forma automatica al compilar.
if __name__ == '__main__':
    unittest.main()

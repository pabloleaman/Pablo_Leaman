# Pablo_Leaman
  El repositorio actual consta de cuatro ficheros escritos en Python, los cuales son utilizados para resolver un problema en particular, con lo cual se lograran obtener resultados que se verificaran mediante pruebas unitarias. Para aquello se utilizará el framework de testing "unittest" para así asegurarse que el codigo este libre de errores. Se realizarán pruebas para el caso que existan y no existan errores. 

  El problema consiste en realizar un programa que reciba un numero natural en particular, para que luego este retorne el termino n y n-1 de la sucesión de Fibonacci. Para aquello se utilizaran 3 ficheros .py, los cuales se describiran a continuación:

- Fibonacci_prueba.py: En este apartado se le pide al usuario ingresar un numero natural. Luego se muestra en la consola un mensaje indicando la posición del numero ingresado en la sucesión de Fibonacci, junto con la posición anterior. Se establece las condiciones iniciales F_0=0 y F_1=1 de la respectiva sucesión, para luego calcular los valores posteriores de la forma que sigue:

						F_n = F_n-1 + F_n-2

- Fib_prueba.py: En este archivo se copiaran las funciones utilizadas en el fichero anterior para obtener las posiciones en la sucesión de Fibonacci, dado el numero ingresado. En particular, se utiliza la función Fib() para retornar el elemento n-esimo de la sucesión y la función Fib_anterior() para retornar el elemento (n-1)-esimo.

- test_fibonacci_fallo.py: En este fichero se realizaran tests con fallos. Se probara un test por cada función, es decir, se realizaran dos tests, uno para la función Fib() y otro para la función Fib_anterior(). Para realizar aquello se debe importar el framework "unittest" y el modulo Fib_prueba.py, donde se encuentran las funciones mencionadas anteriormente. Posteriormente se crea una clase que contendrá todos los tests realizados, los cuales definiran mediante 2 métodos. En cada metodo se utilizan las funciones "assertEqual" y "assertNotEqual". Ambas funciones reciben 2 argumentos, los cuales se comparan, si son diferentes "assertEqual" genera un fallo en caso contrario "assertNotEqual" genera un fallo. En este fichero, en el test para la función Fib() se utiliza "assertNotEqual" para comparar F_6 con 8. Como F_6 == 8, entonces en consola se reporta el fallo, junto con la cantidad total de pruebas.  

- test_fibonacci.py: En este fichero se realizaran los respectivos tests sin fallos. La linea de codigo es similar a la del fichero test_fibonacci_fallo.py. En este caso se testea la función Fib(), utilizando "assertEqual", con lo cual se compara el elemento 7 de la sucesión de Fibonacci con el valor 13. Luego se testea la función Fib_anterior() de igual manera, esta vez comparando el elemento 9 de la misma sucesión con 34. Como F_7 == 13 y F_9 == 34 entonces ambos tests indicaron que no había errores, lo cual se muestra tambien en la consola.          

	Finalmente, para ejecutar los ficheros se acceder, mediante la linea de comandos de la consola, al directorio donde se encuentra el respectivo fichero y luego escribir la orden de ejecución, la cual se describe como sigue:
  
					python  <Nombre_del_Fichero>, para Python 2.7
					python3 <Nombre_del_Fichero>, para Python 3 

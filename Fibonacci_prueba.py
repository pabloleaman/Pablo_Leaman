# Sucesion de Fibonacci qu retorna el n-esimo elemento
def Fib(n):
    
    i=2
    fn0=0           # Elemento 0 de sucesion de Fibonacci
    fn1=1           # Elemento 1 de sucesion de Fibonacci

    global fn  
    fn=fn0+fn1      # Elemento n de sucesion de Fibonacci   

    # Calculo de F_n
    while(i<n):
       fn0=fn1
       fn1=fn
       fn=fn0+fn1
       i=i+1

    # Se imprime el resultado en consola
    global s_fibonacci_n
    s_fibonacci_n= "Posicion del numero ingresado (n) en serie de Fibonacci es: "+ str(fn)

# Sucesion de Fibonacci qu retorna el (n-1)-esimo elemento    
def Fib_anterior(n):
    
    i=2
    fn0=0           # Elemento 0 de sucesion de Fibonacci
    fn1=1           # Elemento 1 de sucesion de Fibonacci 

    global fna
    fna=fn0+fn1     # Elemento n-1 de sucesion de Fibonacci

    # Calculo de F_n-1
    while(i<n-1):
       fn0=fn1
       fn1=fna
       fna=fn0+fn1
       i=i+1

    global s_fibonacci_n_anterior
    s_fibonacci_n_anterior= "Posicion anterior del numero ingresado (n-1) en serie de Fibonacci es: "+ str(fna)
    
    



# Ingreso de numero como consulta desde el teclado
n=input("Ingrese un numero natural\n")

# Llamado de funciones    
Fib(n)
Fib_anterior(n)

# Se imprime el resultado
print s_fibonacci_n
print s_fibonacci_n_anterior

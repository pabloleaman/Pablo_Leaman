# Funcion que retorna elemento n de sucesion de fibonacci
def Fib(n):
    
    i=2
    fn0=0               # Elemento 0 de sucesion de Fibonacci
    fn1=1               # Elemento 1 de sucesion de Fibonacci
    
    global fn
    fn=fn0+fn1          # Elemento n de sucesion de Fibonacci


    # Calculo de F_n
    while(i<n):
       fn0=fn1
       fn1=fn
       fn=fn0+fn1
       i=i+1

    # Retorno de elemento n-esimo de sucesion de Fibonacci
    return fn

# Funcion que retorna elemento n-1 de sucesion de fibonacci
def Fib_anterior(n):
    
    i=2
    fn0=0                  # Elemento 0 de sucesion de Fibonacci
    fn1=1                  # Elemento 1 de sucesion de Fibonacci
    
    global fna
    fna=fn0+fn1            # Elemento n-1 de sucesion de Fibonacci
    
    # Calculo de F_n-1
    while(i<n-1):
       fn0=fn1
       fn1=fna
       fna=fn0+fn1
       i=i+1

    # Retorno de elemento (n-1)-esimo de sucesion de Fibonacci
    return fna  




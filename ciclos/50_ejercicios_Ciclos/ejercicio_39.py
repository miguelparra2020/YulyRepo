# 39.  Se  define  la  serie  de  Fibonacci  como  la  serie  que  comienza  con  
# los  dígitos  1  y  0  y  va sumando progresivamente los dos últimos elementos 
# de la serie, así:0    1    1    2    3    5    8    13    21    34.......Utilizando  
# el  concepto  de  ciclo  generar  la  serie  de  Fibonacci  hasta  llegar  o  sobrepasar  el número 10000

try:
    a = 0 
    b = 1 
    print(a)
    print(b)
    for i in range(20):
        aux = a+b
        a = b
        b = aux
    
        print(aux)
    
    
except ValueError:
    print("Error")
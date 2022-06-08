# 43. Determinar cuántos elementos de la serie de Fibonacci se encuentran entre 1000 y 
# 2000.

try:
    a = 0 
    b = 1 
    print(a)
    print(b)
    cont = 0 
    for i in range(20):
        aux = a+b
        a = b
        b = aux

        if (aux>=1000 and aux<=2000):
            cont += 1
            print(aux)
            print("En la serie fibonacci hay: ",cont,"Numeros, entre 1000 y 2000")
    
    
except ValueError:
    print("Error")
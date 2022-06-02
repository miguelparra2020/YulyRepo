# 47. Leer un número entero y calcular a cuánto es igual la sumatoria de todos los factoriales 
# de los números comprendidos entre 1 y el número leído.
try:
    num = int(input("Por favor ingrese un numero entero"))
    num_2 = num
    suma = 0
    fact = 1
    while(num > 1): 
        
        fact *= num 
        num -= 1
        suma += (fact)
    print("El factorial del numero: ", num_2, "es: ", fact)
    print("La suma de sus factoriales es: ", suma+fact-num_2)
except ValueError:
    print("Error")
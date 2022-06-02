# 46. Leer un número entero y calcular el promedio entero de los factoriales de los enteros 
# comprendidos entre 1 y el número leído.
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
    print("El promedio de sus factoriales es: ", (suma+fact-num_2)/(num_2-1))
except ValueError:
    print("Error")
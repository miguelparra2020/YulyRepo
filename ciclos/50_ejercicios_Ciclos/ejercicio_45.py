# 45. Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el 
# número leído.
try:
    num = int(input("Por favor ingrese un numero entero"))
    suma = 0
    fact = 1
    while(num > 1): 
        
        fact *= num 
        num -= 1
        suma += (fact)
        print("El factorial del numero: ", num, "es: ", fact)
except ValueError:
    print("Error")
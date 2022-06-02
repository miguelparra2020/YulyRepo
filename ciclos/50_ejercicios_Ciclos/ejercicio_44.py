# 44. Leer un número y calcularle su factorial.

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
except ValueError:
    print("Error")

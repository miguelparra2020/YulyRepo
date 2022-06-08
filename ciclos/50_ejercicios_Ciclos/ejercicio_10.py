# 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros
# comprendidos entre 1 y el número leído

try:
    numero = int(input("Por favor ingrese un numero entero"))
    suma = 0
    for i in range(1,numero+1):
        suma += i
    print("La suma de los numeros es: ",suma)
except ValueError:
    print("Error")
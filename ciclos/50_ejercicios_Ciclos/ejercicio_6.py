# 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1
# y cada uno de los dígitos.
try:
    numero_1 = int(input("Por favor ingresar el primer numero entero"))
    numero_2 = int(input("Por favor ingresar el segundo numero entero"))

    for i in range(numero_1, numero_2+1):
        num_1 = i%10
        if num_1==4:
            print("estos numeros terminan en 4, el:    ", i)
except ValueError:
    print("Error")
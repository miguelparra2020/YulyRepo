# 4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.
try:
    numero_1 = int(input("Por favor ingresar el primer numero entero"))
    numero_2 = int(input("Por favor ingresar el segundo numero entero"))

    for i in range(numero_1, numero_2+1):
        print(i)
except ValueError:
    print("Error")
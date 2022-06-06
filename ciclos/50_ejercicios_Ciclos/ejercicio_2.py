# 2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número
# leído.
try:
    numero = int(input("Por favor ingresar un numero entero"))

    for i in range(1, numero+1):
        if i%2==0:
            print(i)
except ValueError:
    print("Error")
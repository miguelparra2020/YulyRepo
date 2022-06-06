# 3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos
# entre 1 y el número leído.
try:
    numero = int(input("Por favor ingresar un numero entero"))

    for i in range(1, numero+1):
        modulos = numero%i
        if modulos==0:
            print(i)
except ValueError:
    print("Error")
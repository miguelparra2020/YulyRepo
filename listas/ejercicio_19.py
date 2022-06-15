# 19. Leer 10 números enteros, almacenarlos en una lista y determinar cuál es el número menor.

try:
    cantidad = int(input("Por favor ingrese la candidad de numeros a solicitar"))
    lista = [int(input("ingrese numero:  ")) for i in range(cantidad)]
    menor = [min(lista[i] for i in range(cantidad))]
    print("De los numeros ingresados, el numero: ",menor[0], "Es el menor ")   
except ValueError:print("Error")
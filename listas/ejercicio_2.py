# 2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el mayor número par leído. 
try:    
    cantidad = int(input("ingresar cantidad de numeros que va a ingresar:  "))
    lista_1 = [int(input("ingrese numero:  ")) for i in range(cantidad)]
    lista_2 = [lista_1.index(max(lista_1[i] for i in range(cantidad) if lista_1[i]%2==0))]
    print(lista_2[0]+1)
except ValueError:print("Error")
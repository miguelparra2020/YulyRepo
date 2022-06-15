# 6. Leer dos números enteros y almacenar en una lista los 10 primeros números 
# primos comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla.

try:
    num_1 = int(input("Por favor ingresar el primer numero:  "))
    num_2 = int(input("Por favor ingresar el segundo numero:  "))
    if num_1<num_2:
        lista = [i for i in range(num_1,num_2)]
    else:
        lista = [i for i in range(num_2,num_1)]
    primo = []
    for i in range(len(lista)):
        contador = 0
        for j in range(2,(lista[i]//2)+1):
            if (lista[i])%j ==0:
                contador += 1
        if contador == 0:
            primo.append(lista[i])
    print(primo)
except ValueError: print("Error")
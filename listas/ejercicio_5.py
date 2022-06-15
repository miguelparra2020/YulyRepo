# 5. Almacenar en una lista de 10 posiciones los 10 primeros números primos comprendidos entre 100 y 300. 
# Luego mostrarlos en pantalla.

try:
    lista = [i for i in range(100,300+1)]
    primo = []
    for i in range(len(lista)):
        contador = 0
        for j in range(2,(lista[i]//2)+1):
            if (lista[i])%j ==0:
                contador += 1
        if contador == 0:
            primo.append(lista[i])
    print(primo[0:10])
except ValueError: print("Error")
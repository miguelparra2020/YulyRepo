# 3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
# el mayor número primo leído.

try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros que va a ingresar     "))
    lista = []
    numero = 0
    mayor = 0
    posicion = 0

    for i in range(0, cantidad):
        lista.append(int(input("Por favor ingrese un numero entero       ")))
        numero = lista[i]
        var = numero/2
        parte_decimal = var - int(var)
        if numero==[2,4]:
            if numero>mayor:
                mayor = numero
                posicion=i
            print("Es primo")
        elif numero < 2:
            print("No es primo")
        elif parte_decimal>0:
            var_2 = numero/3
            var_2_2 = var_2 - int(var_2)
            var_3 = numero/4
            var_3_2 = var_3 - int(var_3)
            var_4 = numero/5
            var_4_2 = var_4 - int(var_4)
            var_5 = numero/6
            var_5_2 = var_5 - int(var_5)
            var_6 = numero/7
            var_6_2 = var_6 - int(var_6)
            var_7 = numero/8
            var_7_2 = var_7 - int(var_7)
            var_8 = numero/9
            var_8_2 = var_8 - int(var_8)
            if (var_2_2>0 and var_3_2>0 and var_4_2>0 and var_5_2>0 and var_6_2>0 and var_7_2>0 and var_8_2>0):
                print("Es primo")
                if numero>mayor:
                    mayor = numero
                    posicion=i
            else:
                print("No es primo")
        else:
            print("No es primo")
    print(mayor, posicion)
except ValueError:
    print("Error")
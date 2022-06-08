# 17. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los
# promedios de los y múltiplos de 5 para valores de x y y leídos

try:
    numero_x = int(input("Por favor ingrese un numero entero mayor a 1 para la variable X "))
    numero_y = int(input("Por favor ingrese un numero entero mayor a 1 para la variable Y "))
    
    suma_x = 0
    suma_y = 0
    contador_x = 0
    contador_y = 0
    
    for i in range(1, numero_x+1):
        modulo = i%10
        if (modulo == 0  or modulo == 2 or modulo == 4 or modulo == 6 or modulo == 8):
            suma_x += i
            contador_x += 1
    promedio_x = suma_x/contador_x
    print("El promedio de la variable X es:    ",promedio_x)
    for j in range(1, numero_y+1):
        modulo = j%10
        if (modulo == 0  or modulo == 5):
            suma_y += j
            contador_y += 1
    promedio_y = suma_y/contador_y
    print("El promedio de la variable Y es:    ",promedio_y)
    print("\n================================")
    if promedio_x>promedio_y:
        print("El promedio de X es Mayor al promedio de Y")
    elif promedio_x==promedio_y:
        print("El promedio de X es Igual al promedio de Y")
    else:
        print("El promedio de Y es Mayor al promedio de X")
except ValueError:
    print("Error")
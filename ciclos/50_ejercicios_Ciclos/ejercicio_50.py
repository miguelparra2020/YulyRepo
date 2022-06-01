#50. Utilizando ciclos anidados generar las siguientes parejas de números
try:
    for i in range(0,7+1):
        if (i>=0 and i<=3):
            j = 1
        if (i>=4 and i<=7):
            j = 2
        print(i,j)
except ValueError:
    print("Error")
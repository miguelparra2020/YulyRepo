# 48. Utilizando ciclos anidados generar las siguientes parejas de enteros
try:
    for i in range(0,9+1):
        if (i==0 or i ==1):
            j=1
        if (i==2 or i ==3):
            j=2
        if (i==4 or i ==5):
            j=3
        if (i==6 or i ==7):
            j=4
        if (i==8 or i ==9):
            j=5
        print(i,j)
except ValueError:
    print("Error")
#49. Utilizando ciclos anidados generar las siguientes ternas de números
try:
    for i in range(1,9+1):
        if (i>=1 and i<=3):
            j =1
        if (i>=4 and i<=6):
            j =2
        if (i>=7 and i<=9):
            j =3
        if (i==1 or i==4 or i==7):
            h =1
        if (i==2 or i==5 or i==8):
            h =2
        if (i==3 or i==6 or i==9):
            h =3
        print(i,j,h)
except ValueError:
    print("Error")
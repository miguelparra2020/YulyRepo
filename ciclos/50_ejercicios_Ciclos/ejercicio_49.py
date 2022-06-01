#49. Utilizando ciclos anidados generar las siguientes ternas de números
try:
    for i in range(1,9+1):
        for j in range(1,3+1,2):
            print(i,j)
except ValueError:
    print("Error")
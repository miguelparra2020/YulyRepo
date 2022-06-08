# 13.  Leer  un entero  y  mostrar  todos los  múltiplos de  5  comprendidos  entre  1  y el número leído.

try:
    numero = int(input("Por favor ingrese un numero entero superior a 1           "))
    
    for i in range(1,numero+1):
        num_1 = i%10
        if (num_1 == 0 or num_1 == 5):
            print(i, "es multiplo de 5")
        
except ValueError:
    print("Error")
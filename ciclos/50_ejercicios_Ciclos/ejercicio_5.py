# 5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre
# ellos.
try:
    numero_1 = int(input("Por favor ingresar el primer numero entero"))
    numero_2 = int(input("Por favor ingresar el segundo numero entero"))

  
    for i in range(numero_1, numero_2+1):
        if i<0:
            num_1 = i*(-1)
            num_2 = num_1%10
            if num_2==4:
                num_3 = num_1*(-1)
                print(" El numero ", num_3, "      Termina en 4")
        else:
            num_1 = i%10
            if  num_1==4:
                print(" El numero ", i, "      Termina en 4")
        
except ValueError:
    print("Error")
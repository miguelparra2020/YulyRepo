# 18.  Leer  dos  números  entero  y  
# mostrar  todos  los  múltiplos  de  5  comprendidos  entre  el menor y el mayor

try:
    numero_1 = int(input("Por favor ingrese el primer numero  entero mayor a 1         "))
    numero_2 = int(input("Por favor ingrese el segundo numero  entero mayor a 1         "))
    
    if (numero_1>=0 and numero_2>=0):
        if numero_1>numero_2:
            for i in range(numero_2,numero_1+1):
                num_1 = i%10
                if (num_1==0 or num_1== 5):
                    print(i)
        elif numero_1<numero_2:
            for j in range(numero_1,numero_2+1):
                num_2 = j%10
                if (num_2==0 or num_2== 5):
                    print(j)
        else:
            print("Son iguales")
    else:
        "Los numeros ingresados son incorrectos"
        
except ValueError:
    print("Error")
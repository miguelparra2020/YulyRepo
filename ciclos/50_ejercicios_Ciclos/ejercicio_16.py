# 16. Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n leído.
try:
    numero = int(input("Por favor ingrese un numero entero mayor a 3 "))
    cont = 0
    suma = 0
    for i in range(1,numero+1):
        num_1 = i//10
        num_2 = i%10
        multiplo = (num_1 + num_2)%3
        if multiplo==0:
            cont += 1
            suma += i
    promedio = int(suma/cont)
    print("Del numero ingresado: ", numero, "Se realiza promedio de los multiplos de 3,")
    print("que hay desde el 1 hasta el ", numero, ", Este promedio es:", promedio)
        
except ValueError:
    print("Error")
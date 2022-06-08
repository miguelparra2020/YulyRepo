# 15. Escribiren pantalla el resultado de sumar los primeros 20 múltiplos de 3

try:
    suma = 0
    for i in range(1,60+1):
        num_1 = i//10
        num_2 = i%10
        multiplo = (num_1 + num_2)%3
        if multiplo==0:
            suma += i
    print(suma)
        
except ValueError:
    print("Error")
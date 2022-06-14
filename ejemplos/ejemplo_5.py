try:
    cant_notas = int(input("Por favor ingrese la cantidad de notas          "))
    cant = cant_notas
    suma = 0 
    notas = 0
    for i in range(1,cant_notas+1):
        if (notas>=0):
            notas = float(input("Por favor ingrese la nota de 0 a 100       "))
            if (notas>100 or notas<0):
                print("Nota incorrecta")
                break
        else:
            print("Notas incorrectas")
        suma += notas
    print("El promedio de las notas es: ",(suma/cant))
    promedio = (suma/cant)
    if (promedio>100 or promedio<0):
        print("Las notas ingresadas SON INCORRECTAS")
    elif(promedio>=0 and promedio<75):
        print("El Aprendiz Perdió")
    else:
        print("El Aprendiz Ganó")
except ValueError:
    print("Error")
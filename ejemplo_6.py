try:
    cant_personas_manana = int(input("Por favor ingrese la cantidad de Personas que ingresan en la mañana          "))
    cant_1 = cant_personas_manana
    cant_personas_tarde = int(input("Por favor ingrese la cantidad de Personas que ingresan en la Tarde          "))
    cant_2 = cant_personas_tarde
    cant_personas_noche = int(input("Por favor ingrese la cantidad de Personas que ingresan en la Noche          "))
    cant_3 = cant_personas_noche
    suma_edades_manana = 0 
    edades_manana = 0
    suma_edades_tarde = 0 
    edades_tarde = 0
    suma_edades_noche = 0 
    edades_noche = 0
    mayor_manana = 0
    mayor_tarde = 0
    mayor_noche = 0
    notificacion_manana = ""
    notificacion_tarde = ""
    notificacion_noche = ""
    if (cant_personas_manana>=0 and cant_personas_tarde>=0 and cant_personas_noche>=0):
        for i in range(1,cant_personas_manana+1):
            if (edades_manana>=0):
                edades_manana = float(input("Por favor ingrese la edad de las personas que ingresan en la mañana       "))
                if edades_manana > mayor_manana:
                    mayor_manana = edades_manana
                if (edades_manana>160 or edades_manana<0):
                    notificacion_manana= "Promedio INCORRECTO!!"
                    print("Edad incorrecta")
                    break
            else:
                print("Notas incorrectas")
            suma_edades_manana += edades_manana
        for j in range(1,cant_personas_tarde+1):
            if (edades_tarde>=0):
                edades_tarde = float(input("Por favor ingrese la edad de las personas que ingresan en la tarde       "))
                if edades_tarde > mayor_tarde:
                    mayor_tarde = edades_tarde
                if (edades_tarde>160 or edades_tarde<0):
                    notificacion_tarde = "Promedio INCORRECTO!!"
                    print("Edad incorrecta")
                    break
            else:
                print("Notas incorrectas")
            suma_edades_tarde += edades_tarde
        for k in range(1,cant_personas_noche+1):
            if (edades_noche>=0):
                edades_noche = float(input("Por favor ingrese la edad de las personas que ingresan en la noche       "))
                if edades_noche > mayor_noche:
                    mayor_noche = edades_noche
                if (edades_noche>160 or edades_noche<0):
                    notificacion_noche = "Promedio INCORRECTO!!"
                    print("Edad incorrecta")
                    break
            else:
                print("Notas incorrectas")
            suma_edades_noche += edades_noche
        print("")
        print(f"La cantidad de personas ingresan en la mañana es: {i} y El promedio es: ",(suma_edades_manana/cant_1),notificacion_manana)
        print(f"La cantidad de personas ingresan en la tarde es: {j} y El promedio es: ",(suma_edades_tarde/cant_2), notificacion_tarde)
        print(f"La cantidad de personas ingresan en la noche es: {k} y El promedio es: ",(suma_edades_noche/cant_3),notificacion_noche)
        print("")
        print("La persona con más edad de la mañana tiene ", mayor_manana,"años")
        print("La persona con más edad de la tarde tiene ", mayor_tarde,"años")
        print("La persona con más edad de la noche tiene ", mayor_noche,"años")
    else:
        print("Cantidad ingresada erronea, debe ser superior a 0")
except ValueError:
    print("Error")


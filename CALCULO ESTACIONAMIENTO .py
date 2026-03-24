horas_auto = int(input("¿Cuantas horas permaneció en el estacionamiento? : "))
tipo_de_vehiculo = input("¿Que vehiculo es , moto, auto o camion? : ")

calculo_moto = horas_auto * 2
calculo_auto = horas_auto * 5
calculo_camion = horas_auto * 10
dcto_moto= calculo_moto - horas_auto*(1-0.10)
dcto_auto= horas_auto*(1-0.10)- calculo_auto
dcto_camion= horas_auto*(1-0.10)- calculo_camion

match tipo_de_vehiculo:
    case "moto":
        print("el costo es 2 por hora")
        if horas_auto >=9:
            print (f"el total con dcto es:{dcto_moto}")
        elif horas_auto >=1 and horas_auto <=8:
            print(f"el total es:{calculo_moto}")
        else:
            print("error")
    case "auto":
        print("el costo es 5 por hora")
        if horas_auto >=9:
            print (f"el total con dcto es:{dcto_auto}")
        elif horas_auto >=1 and horas_auto <=8:
            print(f"el total es:{calculo_auto}")
        else:
            print("error")
    case "camion":
        print("el costo es 10 por hora")
        if horas_auto >=9:
            print (f"el total con dcto es:{dcto_camion}")
        elif horas_auto >=1 and horas_auto <=8:
            print(f"el total es:{calculo_camion}")
        else:
            print("error")

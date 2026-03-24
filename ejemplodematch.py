frutas=input("ELIJE UNA DE LAS FRUTAS PARA SABER SU COLOR, MANZANA, PLATANO, UVA: ")

match frutas:
    case "MANZANA":
        print("ROJO")

    case "PLATANO":
        print("AMARILLO")

    case "UVA":
        print("MORADO")
    case _:
        print("FRUTA DESCONOCIDA")
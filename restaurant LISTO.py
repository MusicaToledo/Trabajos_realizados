#primero van las variables
print("CALCULADORA RESTAURANT")
Costo_cena = float(input("¿Cual es el valor total de la cuenta? : "))
Cant_persona = float(input("¿Cuantas personas son ?: "))
Cant_propina = int(input("¿Que porcentaje de propina desea agregar 5, 10 o 15 % ?: "))
mesero= input("¿Que mesero lo atendió Ana, Juan o Maria ? : ").upper()

#Calculo matematico
       
calculo_propina= Costo_cena * (Cant_propina / 100)
calculo_iva = Costo_cena * 0.19
calculo_por_persona = Costo_cena + calculo_iva + calculo_propina / Cant_persona

#salida de mensaje

print(  "                 "   "Resumen de Cuenta"     )

match mesero:
    case "ANA":
        print("            USTED FUE ATENDIDO POR ANA")
    case "JUAN":
        print("            USTED FUE ATENDIDO POR JUAN")
    case "MARIA":
        print("            USTED FUE ATENDIDO POR MARIA")
    case _ :
        print("                    DESCONOCIDO")   
print("Valor total Neto : $", Costo_cena)
print("Total Iva : $", calculo_iva)
print("Valor total Bruto : $", Costo_cena + calculo_iva)
print("Total propina es : $", calculo_propina)
print("Total por persona es : $", calculo_por_persona)
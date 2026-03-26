energia_total = 1
energia_final = 99



while energia_total < energia_final:
  energia = int(input("Ingrese cantidad de energia cargada: "))
  energia_total += energia
  if energia_total >= energia_final:
    print ("Energia completa")
    break






lado_1 = int(input("longitud 1"))
lado_2 = int(input("lopngitud 2"))
lado_3 = int(input("lopngitud 3"))

if lado_1==lado_2 and lado_2==lado_3:
    print("triangulo equilatero")
elif lado_1==lado_2 and lado_2!=lado_3:
    print("isosceles")
else:
    print("escaleno")
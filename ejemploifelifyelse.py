#condicionales
numero = int(input("Digite un número: "))

#si el numero es mayor a cero sale ese print, es como un verdadero
if numero>0 :
    print("El número es positivo")

#si el numero no es ni postivo ni negativo, es como un intermedio
elif numero==0 :
    print( "El número es 0")

#el numero es menor entonces sale ese print, es como un falso
else:
    print("El número es negativo")

print("Fin del programa")
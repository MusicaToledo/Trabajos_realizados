#ejercicio 1
el_nombre = input('¿Tu nombre? : ').upper() 
print("El nombre es :", el_nombre)

#Ejercicio 2
nombreingreso = input("Ingresa tu nombre: ").upper()
apellido = input("Ingresa tu apellido: ").upper()
cargo = input("Ingresa tu cargo: ").title()

print(f"Hola tu nombre es {nombreingreso} y tu apellido es {apellido} te desempeñas como {cargo}")

#Ejercicio 3
producto = input("¿Que producto lleva? : ")
cantidad = int(input("¿Que cantidad lleva? : "))
precio_unitario = int(input("El precio unitario es : "))

precio_total = precio_unitario*cantidad
calculo_iva = precio_total * 0.19

print("El valor total neto es:", precio_total)
print("Total IVA: ",calculo_iva)
print("El valor total bruto es: ", calculo_iva + precio_total)

#promedio de notas

nota_uno = float(input("Ingresa tu promedio de notas de matematicas : "))
nota_dos = float(input("Ingresa tu promedio de notas de lenguaje : "))
nota_tres = float(input("Ingresa tu promedio de notas de historia : "))
               
#calculo
suma_notas = nota_uno + nota_dos + nota_tres
resultado_promedio = suma_notas / 3

#salida
print("SU PROMEDIO DE NOTAS ES : ", round (resultado_promedio , 1))
#el round se usa para redondear decimales y el uno es para indicar que cantidad de decimales quiero que aparezcan, en caso de no poner el 1, sale un numero entero
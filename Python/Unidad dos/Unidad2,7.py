#Escribe un programa que solicite dos números al usuario y le permita decidir si sumarlos, restarlos, multiplicarlos
#o dividirlos. El programa debe controlar todos los errores posibles.
numero1=int(input("Primer numero:"))
numero2=int(input("segundo numero:"))
eleccion=str(input("sumar, restar, multiplicar o dividir:"))

if eleccion.lower == "sumar":
    print(numero1+numero2)

elif eleccion.lower == "restar":
    print(numero1-numero2)

elif eleccion.lower == "multiplicar":
    print(numero1*numero2)

elif eleccion.lower == "dividir":
    print(numero1/numero2)
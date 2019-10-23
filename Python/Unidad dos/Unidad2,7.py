#Escribe un programa que solicite dos números al usuario y le permita decidir si sumarlos, restarlos, multiplicarlos
#o dividirlos. El programa debe controlar todos los errores posibles.
try:
    numero1=float(input("Primer numero:"))              #Utilizamos un try para meter solo numero y si metemos letras salga un error
    numero2=float(input("segundo numero:"))
except:
    print("Introduce un número!")
    pass
eleccion=input("sumar, restar, multiplicar o dividir:")

if type(eleccion) == str:                     #Definimos el tipo de texto que le vamos a dar a la eleccion de la operacion
    if eleccion == "sumar":                   #Por si en vez de texto metemos un numero nos de un error
        print(numero1+numero2)
    elif eleccion == "restar":
        print(numero1-numero2)
    elif eleccion == "multiplicar":
        print(numero1*numero2)
    elif eleccion == "dividir":            #No se puede dividir entre 0 asi que le ponemos la condicion
        if numero2 == 0:
            print("No se puede dividir entre 0")
        print(numero1/numero2)
    else:
        print("opcion no valida")
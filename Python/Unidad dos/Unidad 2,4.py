#Escribe un programa que solicite un número al usuario e indique si es par o impar
numero = int(input("Introduzca un numero y te diremos si es par o impar:"))
if numero%2 == 0:           #Para saber si es par o impar dividimos el numero entre 2 si de resto da 0 es par y si no es impar
    print("Este numero",numero,"es par")
else:
    print("Este numero",numero,"es impar")
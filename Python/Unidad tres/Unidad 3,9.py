#Da dos	números	enteros	(un	dividendo	y	un	divisor	distinto	de	0)	obtener	su	cociente
#y	el	resto	mediante	restas	sucesivas.


cociente=0
dividendo=int(input("Introduzca un dividendo:")) #31
divisor=int(input("Introduzca un divisor:"))     #5

while dividendo != 0:           #Mientras el dividendo sea diferente a 0 se ejecuta
    if (dividendo >= divisor):  #Si el dividendo es mayor al divisor se hace la cuenta
        cociente+=1             #El cociente cuenta las vueltas que hace para ir restando el resto
        dividendo=dividendo-divisor     #El dividendo es el resto que s eva restando una y otra vez
print("este es el cociente",cociente,"y este el resto",dividendo)   # mostramos el cociente y el dividendo



 
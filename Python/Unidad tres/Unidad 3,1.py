#Escribe	 un	 programa	 que	 lea	 repetidamente	 números	 hasta	 que	 el	 usuario	 introduzca	 “fin”. Una	 vez	 lo	 haya	
#hecho,	muestra	por	pantalla	la	suma total,	la	cantidad y	la	media	de	esos	números.	Si	el	usuario	introduce	otra	
#cosa	que	no sea	un	número ni	“fin”,	debe	mostrar	un	error	y	pasar	al	número	siguiente.
#Introduzca un numero: 40
#Introduzca un numero: a
#Incorrecto.
#Introduzca un numero: 20
#Introduzca un numero: fin
#60 2 30

cantidad=0 #se va a sumar 1 cada vez que introduzca
suma = 0 #se va a sumar el valor de i cada vez que se introduzca

while True:                                 #Utilizamos el while para crear un bucle
    i=input("introduce un numero:")         #introducimos un numero y lo vamos guardando en i
    if i == "fin":                          #Si i es igual a "fin" se acaba el bucle
        media = suma/cantidad               #y si ponemos el fin queremos que nos salga la media la suma y a cantidad
        print(cantidad,suma,media)
    
                                                #Break para salir del bucle                                           
    i=int(i)                                    #definimos que la variable i es de type numero
    cantidad=cantidad+1                         #la cantidad guarda el numero de vueltas que da el bucle puede ser cantidad+=1 
    suma=suma+i
                                                #Y aqui sumamos el total de numero
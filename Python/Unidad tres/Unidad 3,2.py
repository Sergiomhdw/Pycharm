#Modifica	el	programa	anterior	para	que	ahora	muestre	por	pantalla	
# el	máximo	y	mínimo	de	los	números

cantidad=0 #se va a sumar 1 cada vez que introduzca
suma = 0 #se va a sumar el valor de i cada vez que se introduzca
lista=[]

while True:                                 #Utilizamos el while para crear un bucle
    i=input("introduce un numero:")         #introducimos un numero y lo vamos guardando en i
    if i == "fin":                          #Si i es igual a "fin" se acaba el bucle
        media = suma/cantidad               #y si ponemos el fin queremos que nos salga la media la suma y a cantidad
        print(cantidad,suma,media)
        maximo=max(lista)
        minimo=min(lista)
        print(maximo,minimo)
        break                                   #Break para salir del bucle                                           
    i=int(i)                                    #definimos que la variable i es de type numero
    cantidad=cantidad+1                         #la cantidad guarda el numero de vueltas que da el bucle puede ser cantidad+=1 
    suma=suma+i
    lista.append(i)
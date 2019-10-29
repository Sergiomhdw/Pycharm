#Introducir	por	teclado	un	numero	y	mostrar	en	pantalla
#la	serie:	1,	-2,	3,	-4,.........,	n o	–n

i=int(input("Introduce un numero:"))        #Introducimos un numero

for i in range(1,i+1):                      # Un rango de 1 hasta el valor que yo le de                                   
    if i%2 == 0:                            # si el numoro es par lo ponemos negativo
        i=-i
    print(i,sep=" ",end=",")                # mostramos el numero de forma horizontal
    i+=1


        

    



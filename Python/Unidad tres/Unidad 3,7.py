#Introducir	por	teclado	un	numero	y	mostrar	en	pantalla
#la	serie:	1,	-2,	3,	-4,.........,	n o	–n

i=int(input("Introduce un numero:"))

for i in range(1,i+1):
    
    if i%2 == 0:
        i=-i
    print(i,sep=" ",end=",")
    i+=1


        

    



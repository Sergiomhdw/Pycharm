#Introducir	una	serie	de	números	enteros	por	teclado.	
# La	serie	termina	al	introducir	un	0.	Indicar	la	suma	total,	
#y cuántos	han	sido	positivos	y	cuántos	negativos.

lista=[]     #Creo una lista donde se va a almacenar todos los numeros
total=0      #En el total hemos ido sumando 1 para cada dato que hemos dado
negativo=0   #aquí almacenamos los numero negativos
positivo=0   ##aquí almacenamos los numero positivo
while True:             #Abrimos un bucle
    i=int(input("Introduce un numero:"))    #introducimos el numero
    total+=i                                #cada vez que metamos un numero aqui me lo va a sumar
    lista.append(i)                         #Con esta linea introducimos el valor a la lista
    if i < 0:                               #Si el numero es negativo suma uno a la variable negativo
        negativo+=1
    elif i > 0:                             #Si el numero es positivo suma uno a la variable positivo
        positivo+=1
    if i == 0:                              #Cuando le de el valor 0 quiero que me muestre en pantalla todo lo que he ido generando
        print("total",total,"negativos",negativo,"positivos",positivo)
        break                               #IMPORTANTE cerrar el bucle si no al poner 0 seguira pidiendote valores


    
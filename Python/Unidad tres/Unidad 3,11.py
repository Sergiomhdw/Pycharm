#Dado	un	número	entero	positivo	hallar	los	números	perfectos	menores	que	él.	
#Un	número	es	perfecto	si	la	suma	de	sus	divisores,	excepto	él	mismo,	
#es	igual	al	propio	número


suman=0
n1=int(input("Introduzca un numero:"))
lista=[]

for i in range(1, n1):      
    if n1 % i == 0:     
        suman+=i
        lista.append(i)
        print(lista)


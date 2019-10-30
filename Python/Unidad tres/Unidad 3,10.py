#Determinar	si	dos	números	enteros	positivos son amigos,	es	decir,	
# si la	suma de	los	divisores del	1º	excepto	el	mismo	es	igual	al	2º,	y	viceversa.

n1=int(input("Introduce un numero:"))
n2=int(input("introduce un segundo numero:"))

suman1=0                    #Creamos las variables suman1 y 2
suman2=0

for i in range(1, n1):      #Creamos un bucle para sacar los divisores
        if n1 % i == 0:     #so el n1 es divisible entre i == 0
            suman1+=i       # y vamo sumando aqui los numeros

for j in range(1, n2):      #hacemos lo mismo para el segundo numero
        if n2 % j == 0:
            suman2+=j

if suman1 == n2 and suman2 == n1:   #Si la suma del primer numero es igual al asegundo y si la suma
    print("son numeros amigos")     #Del segundo numero es igual al primero ponemos que son amigos
else:                               #Si no pues ponemos que no lo son
    print("no son")

            
           
            


#Usando un bucle	while, mostrar en	pantalla	la	serie:
# 	1,	50,	3,	48,	5,	46,	7,	44....................,	0

listap=list(range(0,51,2))              #en el rango ponemos del 0 al 50 y que vaya de dos en dos
listai=list(range(1,50,2))              # lo mismo pero como son impares empieza en el 1 y termina en el 50
listap.reverse()                        #Le damos la vuelta a la lista par para que sea de 50 a 0 en vez de 0 a 50
i=0
while i in range(0,25):                 # el rango es de 0 a 25 porque los numero van de dos en dos
    print(listai[i],",",listap[i],sep="",end=",")       #mostramos en pantalla los numeros
    i+=1
    

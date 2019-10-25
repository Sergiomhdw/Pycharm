#Usando un bucle	while, mostrar en	pantalla	la	serie:
# 	1,	50,	3,	48,	5,	46,	7,	44....................,	0

listam=list(range(50,0))
listami=list(range(0,50))
maximo=50
minimo=0

while  o<50:
    minimo+=2
    maximo-=2
    listam.append(maximo)
    listami.append(minimo)
    print(o,minimo,maximo,end="0")
    

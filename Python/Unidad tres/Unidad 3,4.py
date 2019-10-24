#Mostrar	los	50	primeros	números	pares	a	partir	del	0,	separados	por	comas
#y	en	orden	creciente.	O	sea:	

for i in range(0,51):              #Creo un bucle con el for in y meto los numeros del rango que tengo
    if i%2 == 0:                   #Seleccionamos el tipo de numero en este caso los pares
        print (i,sep="",end=",")   #el sep es para que los numeros no salgan de verticalmente y el end
                                   #para añadir la ,
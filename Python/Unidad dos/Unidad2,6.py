#Escribe el programa anterior usando solamente dos variables.
lista = [] #Creo una lista para introducir posteriormente

lista.append(int(input("Primer numero:")))      #Utilizamos una lista para meter los numeros y lo almacenamos dentro de esa lista
lista.append(int(input("Segundo numero:")))     #Despues en una variable he puesto que me salga el numero mas altos de los vaolres que doy
lista.append(int(input("Tercer numero")))       #Podemos hacerlo perfectamente si utilizar otra variable podemos utilizar un print del tiron
mayor = max(lista)
print("El numero",mayor,"es el mayor")
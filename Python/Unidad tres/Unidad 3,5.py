#Realizad	el	mismo	ejercicio	anterior	y	además	
# hallar	la	suma	de	todos	los	números	visualizados.

lista=[]            #Creo una lista para guardar todos los valores pares
total=0             #Creo una variable para ir sumando cada valor de I
for i in range(0,51):   #este es el bucle que me da todos los valores pares hasta 50
    if i%2 == 0:
        total+=i        
        lista.append(i)        #el .append añade a la lista que se a creado el valor de i que he introducido

print(lista)
print ("La suma de todos los numeros es igual:",total)  
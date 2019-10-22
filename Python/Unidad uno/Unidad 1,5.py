importe=float(input("Escriba el importe sin iva:"))
iva=int(input("Escriba el IVA:"))

if iva == 4: #si el iva es 4
    iva4=importe+(importe*0.04) #Almacena en una variable el precio aumentado con el iva
    print(iva4) #Aquí lo muestra

elif iva ==10:  #Se utiliza despues de que aparece un if y significa tambien si en esta caso si el iva es 10
    iva5=importe+(importe*0.1)
    print (iva5)

elif iva ==21:
    iva6=importe+(importe*0.21)
    print (iva6)

else: #Se usa else si no se cumple ninguna de las condiciones
    print("Iva incorrecto")
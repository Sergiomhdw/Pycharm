#Reescribe el programa del ejercicio 2.1 usando try y except, de modo que el programa sea capaz de gestionar
#entradas no numéricas mostrando un mensaje y saliendo del programa. A continuación se muestran dos
#ejecuciones del programa:
#Horas de trabajo: 20
#Coste por hora: nueve
#Error, por favor introduzca un número
#Horas de trabajo: cuarenta
#Error, por favor introduzca un número
try:
    horas=int(input("horas trabajada:"))
    costes=int(input("Valor de la hora:"))
except:
    print("Introduce un número!")
    pass  
if  horas > 40:         #Si horas es mayor que 40
    exceso= horas-40    # Aquí guardo las horas que sean superiores a 40 para luego hacerle el 1.5
    costexceso= (exceso*1.5*costes)     #Calculo las horas sobrantes a 40 en este caso en 45 solo 5 horas
    valor= (40*costes+costexceso)       #Calculamos las 40 horas por su valor y le sumamos el las horas restantes que tienen otro valor
    print(valor)
elif horas <=40:        #Si la hora es menor o igual que 40 lo calcula con normalidad
    print(horas*costes)
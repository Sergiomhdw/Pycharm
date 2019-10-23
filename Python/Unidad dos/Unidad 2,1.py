#Reescribe el programa del cálculo del coste de un servicio, 
#para darle 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40. 
# Horas de trabajo: 45 
# Coste por hora: 10 
# Importe total: 475.0 


horas=int(input("horas trabajada:"))
costes=int(input("Valor de la hora:"))
if  horas > 40:         #Si horas es mayor que 40
    exceso= horas-40    # Aquí guardo las horas que sean superiores a 40 para luego hacerle el 1.5
    costexceso= (exceso*1.5*costes)     #Calculo las horas sobrantes a 40 en este caso en 45 solo 5 horas
    valor= (40*costes+costexceso)       #Calculamos las 40 horas por su valor y le sumamos el las horas restantes que tienen otro valor

    print(valor)

elif horas <=40:        #Si la hora es menor o igual que 40 lo calcula con normalidad
    print(horas*costes)

#Reescribe el programa del cálculo del coste de un servicio, para darle 1.5 veces la tarifa horaria para todas las
#horas trabajadas que excedan de 40.
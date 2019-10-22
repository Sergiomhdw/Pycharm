#Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango,
#muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla
#siguiente (el programa debe mostrar la tabla usando tabuladores):
#Puntuación Calificación
#>= 0.9 Sobresaliente
#>= 0.8 Notable
#>= 0.7 Bien
#>= 0.6 Suficiente
#< 0.6 Insuficiente
#Introduzca puntuación:
#Sobresaliente

print("Puntuación\tCalificación")      #Esta es la tabla para tabular usamos el \t\t
print(">=0.9\t\tSobresaliente")
print(">=0.8\t\tNotable")
print(">=0.7\t\tbien")
print(">=0.6\t\tSuficiente")
print("<0.6\t\tInsuficiente")

nota=float(input("Introduce un numero entre 0.0 y 1.0:"))

if nota < 0 or nota >1.0:               #Para definir el rango utilizamos el or para dar mas de una condicion
    print("Ese numero está fuera de rango")
else:                    #He ordenado las condiciones de mayor a menos porque de menos a mayor me cogia 
    if nota < 0.6:       #La segunda condicion siempre y de esta forma uso menos codigo y funciona
        print("Insuficiente")
    elif nota >= 0.9:
        print("Sobresaliente")
    elif nota >= 0.8:
        print("Notable")
    elif nota >= 0.7:
        print("Bien")
    elif nota >= 0.6:
        print("Suficiente")
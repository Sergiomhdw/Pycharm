#Escribe un programa que solicite tres números al usuario y muestre el mayor de ellos.
numero1 = int(input("Primer numero:"))
numero2 = int(input("Segundo numero:"))
numero3 = int(input("Tercer numero:"))

if numero1 > numero2 and numero1 > numero3:     #And lo utilizamos para condicionar una parte cuando pasa una cosa a la vez que otra en este caso
    print(numero1,"Este es el mayor")           #Si el numero 1 es mayor que el segundo y el tercero

elif numero2 > numero1 and numero2 > numero3:
    print(numero2,"Este es el mayor")

elif numero3 > numero1 and numero3 >numero2:
    print(numero3,"Este es el mayor")
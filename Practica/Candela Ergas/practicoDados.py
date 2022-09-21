#Importamos la función randint del método random para obtener números aleatorios.
from random import randint

#Declaramos la funcion -dados-.
def dados():
#Utilizamos el método randint para darle a las variables -random- y -random1- valores numericos enteros aleatorios entre 1 y 6.
    random=randint(1,6)
    random1=randint(1,6)
#Guardamos el resultado de la suma de ambas variables en la variable -suma- para utilizarla en el print, y en el return.
    suma= random+random1
#Mostramos en pantalla los números que salieron en cada variable, y la suma de los mismos.
    print(f'\nSalieron los numeros {random} y {random1}, la suma de tus dados es: {suma}')
#La función -dados- retornará el valor de la variable -suma-, para poder utilizarlo cuando la ejecutemos.  
    return suma

#Declaramos la función -resultado-.
def resultado():
#Utilizamos un input para que el usuario pueda ingresar la opción que quiere y guardarlo en la variable -tirar-.
    tirar=input("Queres tirar los dados? \n 1 = Si \n 2 = No \n")
    #Mientras -tirar- sea igual a "1" ingresará en el siguiente bucle:
    while tirar=="1":
        #1° Guarda en la variable -x- el valor que retorne la ejecución de la función -dados-.
        x= dados()
        #2° Si el valor de la variable -x- es igual a 4 mostrará ese mensaje.
        if x == 4:
            print("Ganaste la mano!")
        #3° Si el valor de la variable -x- es menor a 4 mostrará ese mensaje.
        if x<4:
            print("Perdiste! Se terminó esta partida </3")
        #4° Si el valor de la variable -x- es mayor a 4 mostrará ese mensaje.
        if x>4:
            print("Te pasaste! ")
        #5° Preguntará si quiere jugar de nuevo, y guardará la respuesta como valor actual de la variable -tirar-.
        tirar=input("\nQuerés jugar otra vez? \n 1 = Si \n 2 = No \n")
    #Si -tirar- es igual a 2, mostrará ese mensaje para terminar de jugar.
    if tirar=="2":
        print("Ok, no jugamos más")
    #Si -tirar- no es igual a 1 o a 2, mostrará el mensaje de error y ejecutaremos la función -resultado- para que dé la posibilidad de intentar otra vez
    else: 
        print("Lo que ingresaste no corresponde a ninguna de las opciones, intentá de nuevo")
        resultado()

resultado()
              

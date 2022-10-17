import random #Se importa la librería random

def lanzamiento(): #Se define la función lanzamiento
   
    tiro = input("Indique si quiere lanzar los dados [S/N]:").capitalize()  # Se solicita al usuario que indique si quiere lanzar los dados. Utilizamos la funcion capitalize para normalizar el input en mayúsculas.
   
    if tiro == 'S':  #Si el usuario indica que quiere lanzar los dados, entra al if
        
        dado1 = random.randint(1,6) #Declaramos las variables dado1 y dado2, y ejecutamos la funcion randint para muestra de nros aleatorios
        dado2 = random.randint(1,6)
        sumatoria = (dado1+dado2) #Declaramos variable sumatoria para sumar las variables dados

        comprobacionResultados(sumatoria) #Ejecutamos la funcion comprobacionResultados
    
    else:
        print("Saliendo del juego...") #En el caso de que pulse n, entonces el juego termina
        

def comprobacionResultados(sumatoria): #Definimos la funcion comprobacionResultados, usando como parametro sumatoria

    if sumatoria == 4: #Declaramos la condición: si la sumatoria es igual a 4, entra al if 
        print ("Ganaste!") 
        print (f"La suma de los dos dados es:", sumatoria) #Imprimimos por consola que el usuario ganó y la sumatoria de los dados
        lanzamiento() #Ejecutamos la función lanzamiento para volver a lanzar los dados 

    else: #Si la primer condicion no se cumple, entra en el bucle else
        print ("Perdiste!")
        print (f"La suma de los dos dados es:",sumatoria ) #Imprimimos por consola que el usuario perdió y la sumatoria de los dados
        lanzamiento() #Ejecutamos la función lanzamiento para volver a lanzar los dados 

lanzamiento() #Ejecutamos la función lanzamiento para comenzar el juego

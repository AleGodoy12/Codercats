# Realizar un script en Python para simular un juego de dados, según las siguientes condiciones: 
 
# ➢ El juego consistirá en lanzar dos dados. Para simularlo, debemos obtener dos números aleatorios entre 1 y 6. 
# ➢ Si la suma de los dos dados es 4, el participante gana la mano 
# ➢ Si la suma de los dos dados es menor a 4, el participante pierde y se termina el juego. 
 
# Realizar los comentarios pertinentes en el código para que se entienda la lógica utilizada. 
 
# Mostrar la suma de los números por pantalla y pedirle al usuario que toque una tecla para volver a lanzar los dados. 

import numpy as np #importamos numpy y le asiganamos un alias, np.

# --------------------------------------------------- OPCION N°1 -------------------------------------------------------------------------

# def random_dados(): #declaro una función "random_dados"
#     suma = np.random.randint(1,7) + np.random.randint(1,7) # almacenamos la suma de dos valores random en una variable "suma"
#     if suma == 4: # si la variable suma es igual 4 
#         print(suma, ", Ganaste!") # imprime el valor de la variable suma y un mensaje
#     elif suma < 4: # si la variable suma es menor 4
#         print(suma, ", perdiste!") # imprime el valor de la variable suma y un mensaje
#         return # termina la ejecucion de la función
#     else: # de lo contrario que suma no sea igual a 4 y no sea menor a 4
#         print(suma, ", segui participando...") # imprime el valor de la variable suma y un mensaje
#     operacion = input("Desea tirar el dado? [y/n]: ") # imprime un mensaje, con posibilidad de escribir en consola 
#     if operacion == "y": # si la variable operacion es igual a "y"
#         random_dados() # se llama a la funcion "random_dados" para ejecutar otra vez el codigo
#     else: # de lo contrario que suma no sea "y"
#         return # termina la ejecucion de la función

# random_dados() # se llama a la funcion "random_dados" para ejecutar el codigo.


# --------------------------------------------------- OPCION N°2 -------------------------------------------------------------------------

def suma_dados(cantidad): #definimos una funcion "suma_dados", con el parametro "cantida"
    """Esta función realiza suma de números de forma aleatoria
    según la cantidad de dados pasados como paramentros"""
    suma = 0 # declaramos la variable "suma" con el valor 0
    while cantidad > 0: # realizamos un bucle con la cantidad que se pasa como parametro mientras sea mayor a 0
        suma += np.random.randint(1, 7) #acumulamos numeros random en la variable "suma"
        cantidad -= 1 # le restamos uno a la variable "cantidad"
    return suma # retornamos la variable "suma"

def validar_dados(n, nGanador, nPerdedor): #definimos una funcion "validar_dalos" con los siguientes parametros "n, nGanador, nPerdedor"
    """Esta función define con condicionales que número es el 
    ganador y el perdedor"""
    if n == nGanador: # si la variable "n" es igual a la variable "nGanador"
        print(n, ", Ganaste!") # imprime la variable "n" y un mensaje
    elif n < nPerdedor:  # si la variable "n" es menor a la variable "nPerdedor"
        print(n, ", perdiste!") # imprime la variable "n" y un mensaje
    else: # de lo contrario que "n" no sea igual a "nGanador" y no sea menor a "nPerdedor"
        print(n, ", segui participando...") # imprime la variable "n" y un mensaje

def dados(cantidad, nGanador, nPerdedor): # definimos una funcion "dados"
    """Esta función realiza un bucle preguntando si desea seguir
     jugando hasta que haya un perdedor o no desea jugar más"""
    suma = suma_dados(cantidad) # guardamos en la variable "suma" lo que retorna la funcion "suma_dados"
    validar_dados(suma, nGanador, nPerdedor) # llamamos a la funcion "validar_dados"
    if suma < nPerdedor: return # si la variable "suma" es menor a 4 realiza un return cortando la ejecucion de la funcion
    operacion = input("Desea tirar el dado? [y/n]: ")  # imprime un mensaje, con posibilidad de escribir en consola 
    if operacion == "y": # si la variable operacion es igual a "y"
        dados(2, 4, 4) # se llama a la funcion "dados" para ejecutar otra vez el codigo
    else: # de lo contrario que suma no sea "y"
        return # termina la ejecucion de la función

dados(2, 4, 4)# se llama a la funcion "dados" para ejecutar el codigo.

#help(suma_dados)
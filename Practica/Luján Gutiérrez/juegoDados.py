# El juego consistirá en tirar dos dados
# Debemos obtener dos número aleatorios entre el 1 y el 6
# Si la suma de los dos dados es 4, el participante gana la mano.
# Si la suma de dos dados es menor a 4, el participante pierde y se termina el juego.

# - Realizar los comentarios pertinentes en el codigo para que se entienda la lógica utilizada
# - Mostrar la suma de los números por pantalla y pedirle al usurio que toque una tecla para volver a lanzar los dados.
import numpy as np

def juegoDados (): #creamos una función para que pueda ser reutilizable.
    jugar = input('Toca cualquier tecla para empezar ') #creamos una variable con un input, para pedirle información al usuario.
    while jugar != 'terminar':  #creamos un bucle con la condición de que sólo termine cuando el usuario ingrese "Terminar".
        dados = np.random.randint(1,6,2) #Usamos un módulo importado de numpy, llamado random.radint, en los primeros dos parametros le aclaramos de qué número a qué número tienen que ser los números que salgan y en el tercer parámetro le aclaramos cuántos números queremos que nos de.
        suma = sum(dados) #Creamos una variable donde hacemos la suma los valores que nos trajo el random.radint y guardamos el resultado.
        print('En la tirada salieron los números:', dados, 'y suman', suma) #Imprimimos cuáles fueron los valores de los dados y su suma.
        #Ahora comenzamos un if/elif/else para separar las distintas opciones que nos puede traer el código anterior.
        if suma == 4: #Comenzamos con un if aclarando qué pasaría si la suma de los valores da 4.
            print('FELICIDADES! SACASTE 4! GANASTE!') #Imprimimos el resultado de la condición dada.
            jugar = input('Tocá cualquier tecla para seguir jugando, para terminar escribí x') #Le damos la oportunidad al usuario de seguir jugando y de terminar el juego.
        elif suma < 4: #Acá, con un elif decimos qué pasaría si la suma de los valores fuera menor a 4.
            print('La suma de los dados fue:', suma, '. Perdiste, vuelve a intentar!') #Nuevamente imprimimos el resultado de la condición dada.
            jugar = input('Tocá cualquier tecla para seguir jugando, para terminar escribí \'terminar\'') #Y nuevamente le damos al usuario la opción de seguir jugando o de terminar el juego.
        else: #En el else implicitamente entra cualquier otro resultado de la suma que no cumplan con las condiciones anteriores.
            print('Sacaste:', suma) #Le expresamos al usuario cual fue la suma de los valores recibidos.
            jugar = input('Tocá cualquier tecla para seguir jugando, para terminar escribí \'terminar\'') #Y nuevamente le damos al usuario la oportunidad de seguir jugando o terminar el juego.
juegoDados()

#Versión sin comentar
def juegoDados (): 
    jugar = input('Toca cualquier tecla para empezar ')
    while jugar != 'terminar':
        dados = np.random.randint(1,6,2) 
        suma = sum(dados) 
        print('En la tirada salieron los números:', dados, 'y suman', suma) 
        if suma == 4:
            print('FELICIDADES! SACASTE 4! GANASTE!')
            jugar = input('Tocá cualquier tecla para seguir jugando, para terminar escribí x') 
        elif suma < 4: 
            print('La suma de los dados fue:', suma, '. Perdiste, vuelve a intentar!')
            jugar = input('Tocá cualquier tecla para seguir jugando, para terminar escribí \'terminar\'')
        else:
            print('Sacaste:', suma)
            jugar = input('Tocá cualquier tecla para seguir jugando, para terminar escribí \'terminar\'')
juegoDados()
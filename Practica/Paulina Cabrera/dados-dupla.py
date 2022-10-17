import numpy as np
#1
def tiradaDeDados ():
#2
    jugar = input('Presione cualquier tecla para empezar, para salir presione (Z): ').capitalize()

#3
    while jugar != 'Z':
        dados = np.random.randint(1,7,2)
#4 
        suma = sum(dados)
#5 
        if suma == 4:
#6 
            print(f"¡Felicitaciones te salio 4 GANASTE!")
            jugar = input('Presione una tecla para seguir jugando: ').capitalize()
        elif suma > 4:
#7 
            print(f"¡Lo sentimos! Te salieron los dados: {dados} y la suma es: {suma}")
            jugar = input('Presione una tecla para intentar de nuevo: ').capitalize()
#8 
        else:
            print(f"¡Lo sentimos! No ganaste, te salieron los dados: {dados} y la suma es: {suma}")   
            break              
tiradaDeDados()
print("Juego finalizado")

# COMENTARIOS #

# *1 Definimos la función para que en caso de necesitarla podamos reutilizarla.

# *2 Creamos la variable "jugar" y le asignamos como valor una funcion de tipo input esta misma imprime por pantalla el mensaje y le permite al usuario ingresar datos por consola, en este caso, cuando el usuario presione cualquier tecla el juego inicia, en el mismo mensaje le indicamos que al presionar la letra Z el juego finaliza, al final utilizamos el método "Capitalize ()" que su función es convertir en mayúscula la primera letra ingresada. 

# *3 Iniciamos el ciclo while que se ejecuta mientras lo que ingrese el usuario sea distinto de [Z o z]. 

# *4 Importamos la librería numpy y utilizamos la función random a la cuál le indicamos que devuelva dos valores aleatorios que se encuentren entre el número 1 y el número 6 de dos dados.

# *5 Luego definimos la variable suma y le asignamos como valor la función sum() la cuál su función es sumar los valores pasados por parámetro.

# *6 Utilizamos la condición IF(si) y le decimos que si el resultado de la suma es igual a 4 el jugador gana la partida y tiene nuevamente la chance de seguir jugando.

# *7 En caso de no cumplir con la condición IF(si) usamos la condición ELIF (SI NO) y le indicamos que si el resultado de la suma es mayor a 4 el jugador pierde, pero tiene la chance de seguir jugando.

# *8 Y en caso de no cumplir ninguna de las dos condiciones se ejecuta la condición ELSE en este caso se ejecutara solo si la suma es menor a 4, en caso de ejecutarse el jugador pierde la partida y se termina el juego, para que esto suceda utilizamos el método BREAK que su función es ponerle fin al ciclo while.


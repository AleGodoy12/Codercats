import numpy as np
#1 Definimos la función para que en caso de necesitarla podamos reutilizarla.

def tiradaDeDados ():
    
#2  Colocamos el input "jugar" para que cuando el usuario presione cualquier tecla el juego inicie, en el mismo mensaje le indicamos que al presionar la letra Z el juego finaliza, al final utilizamos el método "Capitalize ()" que su función es convertir en mayúscula la primera letra ingresada. 

    jugar = input('Presione cualquier tecla para empezar, para salir presione (Z): ').capitalize()

#3  Iniciamos el ciclo while que se ejecuta mientras lo que ingrese el usuario sea distinto de [Z o z]. 

    while jugar != 'Z':
#4  Usamos la función random de librería numpy y le indicamos que devuelva dos valores aleatorios que se encuentren entre el número 1 y el número 6.

        dados = np.random.randint(1,6,2)

#5  Luego utilizamos la función sum la cual su función es sumar los valores pasados por parámetro.

        suma = sum(dados)
        
#6  Utilizamos la condición IF(si) y le decimos que si el resultado de la suma es igual a 4 el jugador gana la partida y tiene nuevamente la chance de seguir jugando.

        if suma == 4:
            print(f"¡Felicitaciones te salio 4 GANASTE!")
            jugar = input('Presione una tecla para seguir jugando: ').capitalize()
            
#7  En caso de no cumplir con la condición IF(si) usamos la condición ELIF (SI NO) y le indicamos que si el resultado de la suma es mayor a 4 el jugador pierde, pero tiene la chance de seguir jugando.

        elif suma > 4:
            print(f"¡Lo sentimos! Te salieron los dados: {dados} y la suma es: {suma}")
            jugar = input('Presione una tecla para intentar de nuevo: ') 
            
#8  Y en caso de no cumplirse ninguna de las dos condiciones se ejecuta la condición ELSE en este caso solo si la suma es menor a 4, en caso de ejecutarse el jugador pierde la partida y se termina el juego, para que esto suceda utilizamos el método BREAK que su función es ponerle fin al ciclo while.

        else:
            print(f"¡Lo sentimos! No ganaste,te salieron los dados: {dados} y la suma es: {suma}")   
            break         
        
             
tiradaDeDados()
print("Juego finalizado")




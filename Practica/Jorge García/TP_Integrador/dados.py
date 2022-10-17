import random # Importamos un archivo que contiene las funciones que nos ayudan a generar números aleatorios.
    
# Genera dos números aleatorios entre 1 y 6, los suma y retorna el resultado.
def lanzarDados():
    dadoUno = random.randint(1, 6) # Con el randint se genera un número aleatorio en el rango que se pasa por parámetro.
    dadoDos = random.randint(1, 6)
    sumaDados = dadoUno + dadoDos # Guardamos el valor de la suma de los dados en una variable para luego mostrarla.
    print(f"\nValor dado 1: {dadoUno}")
    print(f"Valor dado 2: {dadoDos}")
    print(f"La suma de los dados es: {sumaDados}")
    return sumaDados

# Se encarga de empezar el juego.
def juegoDeDados(): 
    # Se guarda en la variable respuesta la opción elegida por el usuario.
    respuesta = input("\n==================\n [JUEGO DE DADOS]\n==================\n[1] Lanzar dados\n[2] Salir\nOpción: ") 
    while respuesta == "1": # El bucle se va a repetir mientras el usuario ingrese [1], es decir, que quiera seguir lanzando los dados.       
        resultadoDados = lanzarDados() 
        # Se muestra un mensaje distinto de acuerdo al resultado de lanzar los dados. 
        if resultadoDados == 4:
            print ("\n¡¡¡Ganaste el juego!!!")
        elif resultadoDados < 4:
            print ("\n¡Perdiste! Juego terminado.\n")
            break # Se corta la ejecución del bucle si pierde.
        else:
            print ("\n¡Te pasaste de 4! Inténtalo de nuevo.")
        respuesta = input("\n  ¿Seguir jugando? \n[1] Lanzar los dados \n[2] Salir \nOpción: ")

juegoDeDados()
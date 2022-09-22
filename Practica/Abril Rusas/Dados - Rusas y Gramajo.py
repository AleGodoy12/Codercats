# Trabajo Práctico Integrador : Python  

# Realizar un script en Python para simular un juego de dados, según las siguientes 
# condiciones: 

# ➢  El juego consistirá en lanzar dos dados. Para simularlo, debemos 
# obtener dos números aleatorios entre 1 y 6. 
# ➢ Si la suma de los dos dados es 4, el participante gana la mano 
# ➢  Si la suma de los dos dados es menor a 4, el participante pierde y se 
# termina el juego. 

# Realizar los comentarios pertinentes en el código para que se entienda la lógica 
# utilizada. 

# Mostrar la suma de los números por pantalla y pedirle al usuario que toque una tecla 
# para volver a lanzar los dados.


import numpy as np

#Codigo del juego 
def tirarDados():
    num=np.random.randint(1,7,2)                                      #Tira de dados
    print("Usted ha sacado", num[0],"y",num[1])            
    resultado=num[0]+num[1]                                
    if resultado>4:                                                   #Camino 1(resultado mayor a 4 = vuelve a tirar)  
        print("Obtuvo:",resultado)                         
        opcion=input("Desea volver a tirar? [si/no]")
        if opcion == "si":
            tirarDados()
        else:
            print("Espero que haya disfrutado el juego!")
            return
    elif resultado==4:                                                 #Camino 2(resultado igual a 4 = gana) 
        print("Felicidades! Obtuvo 4. Usted ha ganado :D")
        return
    elif resultado<4:
        print("Lo lamento! Obtuvo ",resultado,". Usted ha perdido :c") #Camino 3(resultado menor a 4 = pierde)
        return

#Ejecucion del juego
tirarDados()
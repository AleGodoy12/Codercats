# # Tuplas

# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima 
# de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.



def consultaMeses():

    meses = ("Enero", "Febrero", "Marzo", "Arbil", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Ocutbre", "Noviembre", "Diciembre")

    numero = int(input("Ingrese un número de mes")) 

    while numero != 0 and numero < len(meses):
        print(meses[numero])
        numero = int(input("Ingrese un número de mes"))

    # Para no dejar enero fuera de la iteración
    # while numero != 0 and numero < len(meses):
    #     numero -= 1
    #     print(meses[numero])
    #     numero = int(input("Ingrese un número de mes"))

consultaMeses()


# 2.  Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

tupla2 = (1, 2, 3, 13, 108, 99, 1, 3, 122, 15, 8, 10, 22, 5, 6, 7, 8, 9, 100, 1, 8, 71)

def inputNum ():

    numero = int(input("Ingrese un número"))
    contador = tupla2.count(numero)
    print(f"El número {numero} se repite {contador} veces")

inputNum()

# 3. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla

tupla3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def inputIndice ():
    
    numero = int(input("Ingrese un índice"))

    if tupla3.index(numero) != ValueError:
        print(tupla3.index(numero))
    else:
        print("No existe ese indice")

inputIndice()
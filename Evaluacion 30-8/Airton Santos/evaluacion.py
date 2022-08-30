# Evaluacion Estructura de datos.

### Se presentan 3 consignas, una por cada estructura de datos donde se busca ademas de la resolucion efectiva, un codigo lo mas escalable y limpio posible.

#### Al finalizar, avisar en hilo por el canal de slack, asi me acerco y de forma aleatoria me explican una de las resoluciones de los ejercicios realizados.

# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

materias = {"Quimica" : "Daniel Alvarez", "Fisica" : "Juana Garay", "Matematica" :"Lucrecia Sanchez", "Literatura" : "Hector Pascal"}

materias.update({"Quimica" : "Cintia Lopez"})
materias.update({"Matematica" : "Juan Lopez"})

print(materias)


# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor

def numerosIngresados():

    listaVacia = []
    numero = int(input("Ingrese un numero"))

    while numero != 0:
        listaVacia.append(numero)
        numero = int(input("Ingrese un numero"))

    listaVacia.sort()
    print(listaVacia)

numerosIngresados()

# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.

tuplaMeses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def comprobacionMeses():
    numero = int(input("Ingrese un numero"))

    while numero != 0:
        if numero >= 1 and numero <= len(tuplaMeses):
            print(tuplaMeses[numero])
            numero = int(input("Ingrese otro numero"))
        else:
            print("Error, no existe el indice")
            numero = int(input("Ingrese otro numero"))

comprobacionMeses()

#Estructura de datos

# 1. A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
numeros=[]
def agregarNum():
    num=int(input("Ingrese un numero: "))
    while num!=0:
        numeros.append(num)
        num=int(input("Ingrese un numero [para finalizar ingrese 0]: "))
    print("Usted ha finalizado")

# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
def borrarNum():
    num=int(input("Ingrese el numero que desee borrar: "))
    if num in numeros:
        numeros.remove(num)
    else:
        print("No es posible eliminar ese numero")

# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
def sumaNum():
    suma=0
    for i in numeros:
        suma += i
    print("La suma de los numeros es: ", suma)

# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
lista=[]
def numMenores():
    num=int(input("Ingrese otro numero: "))
    for i in numeros:
        if i < num:
            lista.append(num)

# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
dic={}
def contarNum():
    for i in numeros:
        if i not in dic:
            veces=numeros.count(i)
            dic.update({i:veces})
    print(dic)

## 2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] 
## Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.
viajeros=[]
def agregarPasajeros():
    pasajero=input("Ingrese el nuevo pasajero: ")
    viajeros.append(pasajero)
    opcion=input("Desea agregar otro pasajero? [si/no]: ").lower
    if opcion=="si":
        pasajero=input("Ingrese el nuevo pasajero: ")
        viajeros.append(pasajero)
    if opcion=="no":
        print("Usted ha finalizado")


## -Agregar ciudades a la lista de ciudades.
ciudades=[]
def agregarCiudad():
    ciudad=input("Ingrese la ciudad: ")
    ciudades.append(ciudad)
    opcion=input("Desea agregar otra ciudad? [si/no]: ").lower
    if opcion=="si":
        ciudad=input("Ingrese la ciudad: ")
        ciudades.append(ciudad)
    if opcion=="no":
        print("Usted ha finalizado")
        
## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
## -Dado el DNI de un pasajero, ver a qué país viaja.
## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
## -Salir del programa.

## 3. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.

# 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.
# Ejercicios 

## 1. A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
## B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
## E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

# A:
listaNum=[]
numUser=int(input("Ingresá de uno los numeros que quieras guardar, para finalizar ingresá 0: "))
while numUser!=0:
    listaNum.append(numUser)
    numUser=int(input("Guardado! Ingresá otro: "))
print("Proceso finalizado!")

# B: 
numEliminar=int(input("Ingresá el número que quieras eliminar: "))
if numEliminar in listaNum:
    listaNum.remove(numEliminar)
else:
    print("Ese número no está en la lista!")

# C:
total=0
for n in listaNum:
    total+= n
print(f"La suma de los elementos {listaNum} es: {total}")

## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

numMayor=int(input("Ingresá el número que quieras que sea el mayor en la nueva lista: "))
listaNueva=[]
for n in listaNum:
    if n<numMayor:
        listaNueva.append(n)
#        print(n)  para que imprima a medida que vaya agregando a la lista
print("Los elementos de la lista nueva son:")
for n in listaNueva:
    print(n)

#E
listaTuplas=[]
for n in listaNum:
    tuplaA=(n,listaNum.count(n))
    if tuplaA not in listaTuplas:
        listaTuplas.append(tuplaA)
print(listaTuplas)

## 2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] 
## Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.
## -Agregar ciudades a la lista de ciudades.
## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
## -Dado el DNI de un pasajero, ver a qué país viaja.
## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
## -Salir del programa.

info=[("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa"),("ccc",34535,"Liverpool"),("Luciana Hernandez", 38981374, "Lisboa"),("Luciana Hernandez", 38981374, "Lisboa")]
ciudades=[("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]

def agregarPasajeros():
    nombre=input("Ingresá el nombre y apellido del pasajero: ").capitalize()
    dni=int(input("Ingresá el DNI del pasajero: "))
    ciudad=input("Ingresá a qué ciudad viaja: ").capitalize()
    tuplaInfo=(nombre,dni,ciudad)
    info.append(tuplaInfo)

def agregarCiudades():
    ciudad=input("Ingresá el nombre de la ciudad: ").capitalize()
    pais=input("Ingresá a que país pertenece: ").capitalize()
    tuplaCiudad=(ciudad,pais)
    ciudades.append(tuplaCiudad)

def ciudadxDni():
    dnip=int(input("ingresá el dni del pasajero: "))
    for dato in info:
        if dnip in dato:
            print(f"{dato[0]} viajará a {dato[2]}")
def cantxCiudad():
    ciudadU=input("Ingrese una ciudad: ").capitalize()
    total=0
    for dato in info:
        if ciudadU in dato:
            total+=1
    print(f"{total} pasajeros viajan a {ciudadU}")

def paisxDni():
    dnip=int(input("ingresá el dni del pasajero: "))
    for dato in info:               #Recorro los datos para obtener qué pasajero es
        if dnip in dato:            
            ciudad=dato[2]          #Obtengo la ciudad de ese pasajero
            for x in ciudades:      #Recorro la lista para encontrar el indice de la ciudad, y llamar a su país
                if ciudad in x:
                    print(f"{dato[0]} viaja a {x[1]}")

def cantxPais():
    paisP=input("Ingresá un país: ").capitalize()
    pais=paisP
    for x in ciudades:
        if paisP in x:
            paisP=x[0]
    total=0
    for pasajero in info:
        if paisP in pasajero:
            total+=1
    print(f"{total} pasajeros viajan a {pais} ")
        
print("Opciones disponibles: \n [1] Agregar pasajeros a la lista de viajeros.\n [2] Agregar ciudades a la lista de ciudades.\n [3] Dado el DNI de un pasajero, ver a qué ciudad viaja. \n [4] Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.\n [5] Dado el DNI de un pasajero, ver a qué país viaja. \n [6] Dado un país, mostrar cuántos pasajeros viajan a ese país. \n [7] Salir del programa.")

opcion=int(input("Ingresá el nro de operación que querés realizar: "))
while opcion:
    if opcion==1:
        agregarPasajeros()
        opcion=int(input("Ingresá el nro de operación que querés realizar: "))
    if opcion==2:
        agregarCiudades()
        opcion=int(input("Ingresá el nro de operación que querés realizar: "))
    if opcion==3:
        ciudadxDni()
        opcion=int(input("Ingresá el nro de operación que querés realizar: "))
    if opcion==4:
        cantxCiudad()
        opcion=int(input("Ingresá el nro de operación que querés realizar: "))
    if opcion==5:
        paisxDni()
        opcion=int(input("Ingresá el nro de operación que querés realizar: "))
    if opcion==6:
        cantxPais()
        opcion=int(input("Ingresá el nro de operación que querés realizar: "))
    if opcion==7:
        break

## 3. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.
agenda={}
n=int(input("Querés agendar un número nuevo? \n [1] Si \n [2] No \n Ingresá el nro de opción: "))
while n == 1: 
    nombre=input("Ingresá el nombre que querés agendar: ")
    if nombre in agenda:
        print("Ups!Ese nombre ya está agendado,probá con otro")
        nombre=input("Ingresá el nombre que querés agendar: ")
        nro=int(input("Ingresá su número: "))
        agenda.update({nombre:nro})
        print("Perfecto! El contacto fué agendado")
    if nombre not in agenda:
        nro=int(input("Ingresá su número: "))
        agenda.update({nombre:nro})
        print("Perfecto! El contacto fué agendado")
    n=int(input("Querés agendar otro contacto? \n [1] Si \n [2] No \n Ingresá el nro de opción: "))
print(agenda)


## 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

cesta={}
costeTotal=0
agregar=input("Desea agregar un articulo a la cesta?[Si/No] : ").capitalize()
while agregar=="Si":
    art=input("Ingresá el nombre del artículo: ")
    precio=int(input("Ingresá el precio del artículo: "))
    cesta.update({art:precio})
    costeTotal+=precio
    agregar=input("Desea agregar otro articulo a la cesta?[Si/No] : ").capitalize()
if agregar=="No":
    print(f"La lista de productos es {cesta} y su costo total es {costeTotal}")

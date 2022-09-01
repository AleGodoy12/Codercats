#Estructura de datos

# 1. A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
numeros=[1,2,3,4,5,6,7,8,9]
def agregarNum():
    num=int(input("Ingrese un numero: "))
    while num!=0:
        numeros.append(num)
        num=int(input("Ingrese un numero [para finalizar ingrese 0]: "))
    return ("Los números se han agregado exitosamente")

# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
def borrarNum():
    num=int(input("Ingrese el numero que desee borrar: "))
    if num in numeros:
        numeros.remove(num)
        return ("Número borrado")
    else:
        return("No es posible eliminar ese numero")

# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
def sumaNum():
    suma=0
    for i in numeros:
        suma += i
    return ("La suma de los numeros es: ", suma)

# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
lista=[]
def numMenores():
    num=int(input("Ingrese un numero: "))
    for i in numeros:
        if i < num:
            lista.append(i)
    return ("Los numeros menores a ",num," son: ",lista)

# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
numeros=[1,1,2,3,4,5,6,6,6,7]
def contarNum():
    lista=[]
    for i in numeros:
        veces=numeros.count(i)
        tupla= i,veces
        if tupla not in lista:
            lista.append(tupla)
    return lista

#Programa con todas las funciones integradas:

opcion=None
while opcion!=6:
    opcion=int(input("[1] Agregar números\n[2] Borrar números\n[3] Números menores a ...\n[4] Sumar números\n[5] Contar número\n[6] Salir\nMarque una opción:"))
    if opcion==1:
        print(agregarNum(),"\n")
    if opcion==2:
        print(borrarNum(),"\n")
    if opcion==3:
        print(numMenores(),"\n")
    if opcion==4:
        print(sumaNum(),"\n")
    if opcion==5:
        print(contarNum(),"\n")
print("Programa finalizado")

## 2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] 
## Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.
datos=[("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]
destinos=[("Liverpool","Inglaterra"),("Buenos Aires","Argentina"),("Glasgow","Escocia"), ("Lisboa", "Portugal")]

def agregarPasajero():
    nombre=input("Ingrese su nombre: ").capitalize()
    dni=int(input("Ingrese su número de documento: "))
    ciudad=input("Ingrese la ciudad de destino: ").capitalize()
    tupla=(nombre,dni,ciudad)
    datos.append(tupla)
    print("El pasajero ha sido agregado")
    opcion=input("Desea agregar otro pasajero? [si/no]: ").lower()
    if opcion=="si":
        agregarPasajero()

## -Agregar ciudades a la lista de ciudades.
def agregarCiudad():
    pais=input("Ingrese la pais de destino: ").capitalize()
    ciudad=input("Ingrese la ciudad de destino: ").capitalize()
    tupla=(ciudad,pais)
    destinos.append(tupla)
    print("La ciudad ha sido agregada correctamente")
    opcion=input("Desea agregar otra ciudad? [si/no]: ").lower()
    if opcion=="si":
        agregarCiudad()
        
## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
def buscarCiudad():  
    dni=int(input("Ingrese el dni del pasajero: "))
    for dato in datos:
        if dni==dato[1]:
            return dato[2]

## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
def cantPasajerosCiudad(ciudad):
    i=0
    for dato in datos:
        if dato[2]==ciudad:
            i+=1
    display=("La cantidad de pasajeros que viaja a esa ciudad son: ",i)
    return display

## -Dado el DNI de un pasajero, ver a qué país viaja.
def buscarPais():  
    dni=int(input("Ingrese el número de documento:"))
    for dato in datos:
        if dni==dato[1]:
            ciudad=dato[2]
            for destino in destinos:
                if ciudad==destino[0]:
                    return destino[1]

## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
def cantPasajerosPais():
    pais=input("Ingrese un país: ").capitalize()
    for destino in destino:
        if destino[1]==pais:
            ciudad=destino[0]
            cant=0
            for dato in datos:
                if dato[2]==ciudad:
                    cant+=1
            display=("La cantidad de pasajeros que viaja a ese país son: ",cant)
            return display
## -Salir del programa.

#Programa con funciones integradas
opcion=None
while opcion!=6:
    opcion=int(input("[1] Agregar pasajeros\n[2] Agregar destino\n[3] Buscar ciudad\n[4] Cantidad de pasajeros que viajan a una ciudad\n[5] Cantidad de pasajeros que viajan a un país\n[6] Salir\nMarque una opción:"))
    if opcion==1:
        print(agregarPasajero(),"\n")
    if opcion==2:
        print(agregarCiudad(),"\n")
    if opcion==3:
        print(buscarCiudad(),"\n")
    if opcion==4:
        ciudad=input("Ingrese una ciudad: ")
        print(cantPasajerosCiudad(ciudad),"\n")
    if opcion==5:
        print(cantPasajerosPais(),"\n")
print("Programa finalizado")

## 3. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.
agenda={}
def agregarNumeros():
    contacto=input("Ingrese un contacto: ")
    if contacto in agenda:
        print("El contacto ya existe")
    else:
        numero=int(input("Ingrese el numero: "))
        agenda.update({contacto:numero})
        print("Contacto agregado exitosamente")
        opcion=input("Desea agregar otro contacto? [si/no]: ").lower()
        if opcion=="no":
            print( "Usted ha finalizado")
        elif opcion=="si":
            agregarNumeros()

# 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.
def carrito():
    ticket={}
    articulo=input("Ingrese un articulo: ")
    precio=int(input("Ingrese el precio: "))
    ticket.update({articulo:precio})
    opcion=input("Desea agregar otro articulo? [si/no]: ").lower()
    if opcion=="no":
        total=sum(ticket.values())
        return ("El total es: $",total)
    elif opcion=="si":
        carrito()
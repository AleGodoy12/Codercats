# Ejercicios 

## 1. A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
## B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
## E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

def pedirNumeros(lista):
    while True:
        num = int(input("Ingresa un número [0 para salir]: "))
        if(num == 0): break
        lista.append(num)
    return lista

def eliminarNumero(lista, numero):
    if(numero in lista):
        lista.remove(numero)
        return True
    return False

def sumatoria(lista):
    acumulador = 0
    for i in lista:
        acumulador += i
    return acumulador

def filtrarListaPorNumero(lista, numero):
    listaFiltrada = []
    for i in lista:
        if(i < numero):
            listaFiltrada.append(i)
    return listaFiltrada
        
def calcularOcurrencias(lista):
    listaOcurrencias = []
    for i in lista:
        tuplaAux = i , lista.count(i)
        if(tuplaAux not in listaOcurrencias):
            listaOcurrencias.append(tuplaAux)
    return listaOcurrencias

opcion = None
listaNumeros = [5,16,2,5,57,5,2]
while opcion != 'F':
    opcion = input("\n      --- Menú ---"
                   "\n[A] Ingresar números"
                   "\n[B] Eliminar número"
                   "\n[C] Calcular sumatoria"
                   "\n[D] Filtrar números"
                   "\n[E] Mostrar ocurrencias"
                   "\n[F] Salir"
                   "\nOpción: ").upper()

    if(opcion == 'A'):
        listaNumeros = pedirNumeros(listaNumeros)
        print(listaNumeros)
    elif(opcion == 'B'):
        numUsr = int(input("Ingresa el número a eliminar: "))
        seElimino = eliminarNumero(listaNumeros, numUsr)
        if(not seElimino):
            print("\nNo se pudo eliminar el número ingresado\n")
        print(listaNumeros)
    elif(opcion == 'C'):
        print(f"\nSumatoria: {sumatoria(listaNumeros)}")   
    elif(opcion == 'D'):
        numUsr = int(input("Ingresa un número: "))
        nuevaLista = filtrarListaPorNumero(listaNumeros, numUsr)
        if(len(nuevaLista) > 0):
            for i in nuevaLista:
                print(i)
        else:
            print(f'\nNo hay números menores que {numUsr}')
    elif(opcion == 'E'):
        print(calcularOcurrencias(listaNumeros))


## 2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] 
## Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.
## -Agregar ciudades a la lista de ciudades.
## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
## -Dado el DNI de un pasajero, ver a qué país viaja.
## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
## -Salir del programa.

def extraerCiudades(listaDestinos):
    ciudades = []
    for i in listaDestinos:
        ciudades.append(i[0])
    return ciudades

def agregarPasajero(listaPasajeros, destinos):
    nombreUsr = input("Nombre: ").capitalize()
    dniUsr = int(input("DNI: "))
    ciudadUsr = input("Ciudad: ").capitalize()
    if ciudadUsr in extraerCiudades(destinos):
        listaPasajeros.append((nombreUsr, dniUsr, ciudadUsr))
        return True
    return False

def agregarDestino(listaDestinos):
    paisUsr = input("País: ").capitalize()
    ciudadUsr = input("Ciudad: ").capitalize()
    listaDestinos.append((ciudadUsr, paisUsr))
    
def buscarCiudadPorDNI(listaPasajeros, dni):
    for pasajero in listaPasajeros:
        if pasajero[1] == dni:
            return pasajero[2]
    return None

def buscarPaisPorDNI(listaPasajeros, destinos, dni):
    ciudad = buscarCiudadPorDNI(listaPasajeros, dni)
    if ciudad != None:
        for i in destinos:
            if i[0] == ciudad:
                return i[1]
    return None

def ocurrenciaPorCiudad(listaPasajeros, ciudad):
    contador = 0
    for pasajero in listaPasajeros:
        if pasajero[2] == ciudad:
            contador += 1
    return contador

def ocurrenciaPorPais(listaPasajeros, listaDestinos, pais):
    contador = 0
    for pasajero in listaPasajeros:
        for destino in listaDestinos:
            if pasajero[2] == destino[0] and destino[1] == pais:
                contador += 1
    return contador

opcion = None
pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa"), ("Luis Hernandez", 58960374, "Manchester")]
destinos = [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España"), ("Manchester", "Inglaterra")]
 
while opcion != '7':
    opcion = input("\n      --- Menú ---"
                    "\n[1] Agregar pasajero"
                    "\n[2] Agregar destino"
                    "\n[3] Buscar ciudad destino por DNI del pasajero"
                    "\n[4] Mostrar cantidad de pasajeros por ciudad"
                    "\n[5] Buscar país destino por DNI del pasajero"
                    "\n[6] Mostrar cantidad de pasajeros por país"
                    "\n[7] Salir"
                    "\nOpción: ").upper()

    if(opcion == '1'):
        if(agregarPasajero(pasajeros, destinos)):
            print("\n¡Se agrego el pasajero!")
        else:
            print("\nNo esta disponible la ciudad.")
    elif(opcion == '2'):
        agregarDestino(destinos)
        print(destinos)
    elif(opcion == '3'):
        dniUsr = int(input("DNI a buscar: "))
        ciudad = buscarCiudadPorDNI(pasajeros, dniUsr)
        if(ciudad != None):
            print(f'\nCiudad destino del pasajero con DNI {dniUsr}: {ciudad}')
        else:
            print('\nDNI inexistente')
    elif(opcion == '4'):
        ciudad = input("Ciudad a buscar: ").capitalize()
        print(f"\nCantidad de pasajeros que viajan a {ciudad}: {ocurrenciaPorCiudad(pasajeros, ciudad)}")
    elif(opcion == '5'):
        dniUsr = int(input("DNI a buscar: "))
        pais = buscarPaisPorDNI(pasajeros, destinos, dniUsr)
        if(pais != None):
            print(f'\nPaís destino del pasajero con DNI {dniUsr}: {pais}')
        else:
            print('\nDNI inexistente')
    elif(opcion == '6'):
        pais = input("País a buscar: ").capitalize()
        print(f"\nCantidad de pasajeros que viajan a {pais}: {ocurrenciaPorPais(pasajeros, destinos, pais)}")

## 3. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.

agenda = {}
respuesta = None
while respuesta != 'no':
    nombre = input("Nombre: ").capitalize()
    if nombre not in agenda:
        agenda[nombre] = input("Telefono: ")
    else: 
        print(f"\n{nombre} ya esta en la agenda\n")
    respuesta = input("¿Agregar otro contacto? [si/no]: ").lower()
print(agenda)

## 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

carrito = {}
respuesta = None
while respuesta != 'no':
    articulo = input("Artículo: ").capitalize()
    carrito[articulo] = float(input("Precio: "))
    respuesta = input("¿Agregar otro artículo? [si/no]: ").lower()

print('\nCesta de compras\n')
for articulo in carrito.keys():
    print(f"{articulo} -> {carrito[articulo]}$")
print(f"Coste total: {sum(carrito.values())}\n")
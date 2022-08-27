# Ejercicios 

## 1. A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
## B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
## E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
 
# sumatoria = 0
# lista = []
# lista_tupla = []

# while True:
#     number = int(input("Ingrese un número: "))
#     if number == 0:
#         break
#     else: 
#         lista.append(number)


# eliminar = int(input("Ingrese un número para eliminar: "))
# if eliminar in lista:
#     lista.remove(number)
#     print(f"La lista queda asi: {lista}")
# else:
#     print("El numero ingresado no se encuentra en la lista")


# for i in lista:
#     sumatoria += i
# print(f"La sumatoria de los elementos de la lista es: {sumatoria}")


# number2 = int(input("Ingresse un numero: "))
# lista_nueva = [x for x in lista if x < number2]
# print("Elementos de la lista original menores a", number2)
# [print(f"Elemento de nueva lista: {a}") for a in lista_nueva]

# set_lista = set(lista)
# for a in set_lista:
#     lista_tupla.append((a, lista.count(a)))
# print(lista_tupla)



## 2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] 
## Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.
## -Agregar ciudades a la lista de ciudades.
## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
## -Dado el DNI de un pasajero, ver a qué país viaja.
## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
## -Salir del programa.

# pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa"), ("Ariel Arapa", 42804188, "Jujuy"), ("Vanesa Anahi", 48190283, "Jujuy")]
# ciudades = [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España"), ("Jujuy", "Argentina")]

# def registrar_pasajero(lista):
#         nombre = input("Ingrese su nombre: ")
#         dni = int(input("Ingrese su D.N.I.: "))
#         ciudad_viajar = input("Ingrese la ciudad a donde se dirige: ")
#         lista.append((nombre, dni, ciudad_viajar))
#         print("Pasajero registrado!")
# def registrar_ciudad(lista):
#         ciudad = input("Ingrese una ciudad: ")
#         pais = input("Ingrese el pais de la ciudad: ")
#         lista.append((ciudad, pais))
#         print("Pais registrado!")
# def consulta_de_ciudad(lista):
#     dni_validar = int(input("Ingrese un numero de dni: "))
#     for a in lista:
#         if a[1] == dni_validar:
#             return f"El pasajero {a[0]} viaja a la ciudad de {a[2]}"
# def viajeros_segun_ciudad(lista):
#         cont = 0
#         ciudad_validar = input("Ingrese una ciudad para buscar: ")
#         for x in lista:
#             if ciudad_validar == x[2]:
#                 cont += 1
#         return f"A la ciudad de {ciudad_validar} viajan {cont} pasajeros."
# def consulta_de_pais(lista, lista2):
#         dni_para_pais = int(input("Ingrese un numero de dni: "))
#         for a in lista:
#             if a[1] == dni_para_pais:
#                 for p in lista2:
#                     if a[2] == p[0]:
#                         return f"El pasajero {a[0]} viaja al pais: {p[1]}"
# def viajeros_segun_pais(lista, lista2):
#         pais_validar = input("Ingrese un pais para buscar: ")
#         cont = 0
#         for p in lista2:
#             if p[1] == pais_validar:
#                 for x in lista:
#                     if p[0] == x[2]:
#                         cont += 1
#         return f"Al pais: {pais_validar} viajan {cont} pasajeros."

# while True:
#     print("~"*120)
#     operacion = int(input("""Menu con las siguientes operaciones: 
#     [1] : Agregar paasajeros a lista de viajeros.
#     [2] : Agregar ciudades a la lista de ciudades.
#     [3] : Dado el DNI de un pasajero, ver a qué ciudad viaja.
#     [4] : Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#     [5] : Dado el DNI de un pasajero, ver a qué país viaja.
#     [6] : Dado un país, mostrar cuántos pasajeros viajan a ese país.
#     [0] : Salir del programa.

#     ¿Que operacion desea ejecutar?: """))

#     if operacion == 1:
#         registrar_pasajero(pasajeros)

#     elif operacion == 2:
#         registrar_ciudad(ciudades)
    
#     elif operacion == 3:
#         print(consulta_de_ciudad(pasajeros))

#     elif operacion == 4:
#         print(viajeros_segun_ciudad(pasajeros))

#     elif operacion == 5:
#         print(consulta_de_pais(pasajeros, ciudades))

#     elif operacion == 6:
#         print(viajeros_segun_pais(pasajeros, ciudades))

#     elif operacion == 0:
#         print("Fin de la ejecución")
#         break



## 3. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.
# dicc = {}
# while True:
#     nombre = input("Ingrese un nombre: ")
#     if nombre == "Salir" or nombre == "salir":
#         break
#     if dicc.get(nombre) == None:
#         numero = int(input("Ingrese el numero de telefono: "))
#         dicc.update({nombre : numero})
#     else:
#         print("Ya ingresaste este contacto!")
# print(dicc)


## 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

cesta = {}
contador = 0
while True:
    nombre = input("Ingrese un nombre del producto: ")
    if nombre == "Salir" or nombre == "salir":
        break
    if cesta.get(nombre) == None:
        numero = int(input("Ingrese el coste del producto: "))
        cesta.update({nombre : numero})
    else:
        print("Ya ingresaste este producto!")

print("Lista de compras: ")
for i in cesta:
    contador += cesta[i]
    print(i, ": $", cesta[i])
print("Precio total de compra: $" + str(contador))
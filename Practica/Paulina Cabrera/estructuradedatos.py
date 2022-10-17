# Ejercicios 


# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.


# numeros = int(input("Ingrese un numero, para salir ingrese [0]: "))
# lalista = []
# while numeros != 0:
#     lalista.append(numeros)
#     numeros = int(input("Ingrese un numero, para salir ingrese: [0]"))
#     print(lalista)
# print("se termino el programa")

## B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

# numero2= int(input("Ingrese el número que quiere buscar dentro de la lista: "))

# if numero2 in lalista:
#     lalista.remove(numero2)
#     print(f"Se elminara el elemento: {numero2}")
#     print(f"La lista modificada quedo asi: {lalista}")
# else:
#     print("El número ingresado no se encontraba en la lista") 

   
## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.

# def sumalista():
#     sumatotal=0
#     for num in lalista:
#         sumatotal += num
#     return sumatotal
# print(f"La suma total de la lista es igual a {sumalista()}")

## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

# num3 = int(input("Ingrese otro numero y le devolveremos los elementos de menor tamaño: "))
# def numchicos(lalista, num3):
#     nueva=[]
#     for nb in lalista:
#         if nb<num3:
#             nueva.append(nb)
#     return nueva
# print(lalista)
# print(f"Los numeros mas chicos que {num3}: {numchicos(lalista, num3)}")


# ## E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

# repeticiones=  []
# def aparece():
#     for a in lalista:
#        if lalista.count(a) >1:
#           repeticiones.append([a,lalista.count(a)])
#     return repeticiones
# print(aparece())



## 2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). 
## Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.

# viajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]
# paises= [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]

# def guiaturista():
#     nombre= input("Indiqueme el nombre del pasajero: ")
#     dni = int(input("Ingrese el numero de DNI del pasajero: "))
#     destino = input("Indique el destino: ")
#     viajeros.append((nombre,dni,destino))
#     pregunta = input("Desea agregar pasajeros a la lista [S/N]").capitalize
#     while pregunta == "S":
#         nombre= input("Indiqueme el nombre del pasajero: ")
#         dni = int(input("Ingrese el numero de DNI del pasajero: "))
#         destino = input("Indique el destino: ")
#         viajeros.append((nombre, dni, destino))
#         print(viajeros)
#         pregunta = input("Desea  seguir agregando pasajeros a la lista [S/N]")
        
#     print("Usted ha salido de la guia turistica")
      

## -Agregar ciudades a la lista de ciudades.

# paises= [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]
# def ciudadesFun(p):
#     ciudad = input("Indique el nombre de la ciudad que quiere ingresar: ")
#     pais = input("Ingrese el pais al que corresponde la ciudad ingresada: ")
#     p.append((ciudad,pais))
#     agregar = input("¿Desea seguir agregando ciudades? [S/N]")
#     while agregar == "S":
#         ciudad = input("Indique el nombre de la ciudad que quiere ingresar ")
#         pais = input("Ingrese el pais al que corresponde la ciudad ingresada")
#         p.append((ciudad,pais))
#         agregar = input("¿Desea seguir agregando ciudades? [S/N] ")
#         print(paises)


# ## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
# def buscarCiudad(viajeros):
#     dni=int(input("Ingrese el DNI del pasajero: "))
#     for viaje in viajeros:
#         if viaje[1]==dni:
#             return f"La ciudad de destino es: {viaje[2]}"

# ## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.

# def ciudad_coincidencia(viajeros):
#     ciudad= input("Ingrese la ciudad que busca:")
#     viajan = 0
#     for i in viajeros:
#         if i[2]== ciudad:
#             viajan+=1
#     return f"A la ciudad de {ciudad} viajan: {viajan} pasajeros " 


# ## -Dado el DNI de un pasajero, ver a qué país viaja.
 # def buscar_pais(viajeros, paises):
#     dni_buscado = int(input("Ingrese su numero de DNI: "))
#     for dni in viajeros:
#         if dni[1] == dni_buscado:
#             for i in paises:
#                 if dni[2] == i[0]:
#                     return f"El pais de destino es: {i[1]}"

# ## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
# def pais_coincidencia(paises):
#     pais= input("Ingrese el pais que busca:")
#     viajan = 0
#     for i in paises:
#         if i[1]== pais:
#             viajan+=1
#     return f"Al pais {pais} viajan: {viajan} pasajeros " 


# while True:
#    a = int(input("""Elija alguna de las siguientes opciones: 
#                  [1]Agregar pasajeros a la lista de viajeros 
#                  [2]Agregar ciudades a la lista de ciudades 
#                  [3]Dado el DNI de un pasajero, ver a qué ciudad viaja
#                  [4]Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad 
#                  [5]Dado el DNI de un pasajero, ver a qué país viaja 
#                  [6]Dado un país, mostrar cuántos pasajeros viajan a ese país 
#                  [7]Salir
#                  Opción: """))
#    if (a==1):
#        print(guiaturista())
#        print(viajeros)
#    if(a==2):
#        print(ciudadesFun(paises))
#        print(paises)
#    if(a==3):
#        print(buscarCiudad(viajeros))
#    if(a==4):
#        print(ciudad_coincidencia(viajeros))
#    if(a==5):
#        print(buscar_pais(viajeros, paises))
#    if(a==6):
#        print(pais_coincidencia(paises))
#    if(a==7):
#        print("Gracias por usar la guia turistica de pau <3")
#        break
        

## 3. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.


# dic = {"Isabela": 1124587, "Monica": 1125487759}

# nombre = input("Indique su nombre: ")
# telefono = int(input("Indique su numero telefonico: "))
# agregar= input("¿Desea seguir agregando nombre y numeros? [S/N]: ")
# dic.update({nombre:telefono})
# while agregar == "S":
#     nombre = input("Indique su nombre: ")
#     telefono = int(input("Indique su numero telefonico: "))
#     if nombre in dic:
#         print("No es posible agregar nombres repetidos")
#     else:
#         dic.update({nombre:telefono})
#     agregar= input("¿Desea seguir agregando nombre y numeros? [S/N]: ")
# print(dic)

## 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato


# carritoCompras = {}

# seguir =True
# while seguir:
#     articulo = input("Ingrese el producto que quiere agregar al carrito de compras: ")
#     precio = float(input("Ingrese el precio del producto "))
#     seguir= input("¿sigue agregando? [S/N] ") == "S"
#     carritoCompras.update({articulo:precio})
# total = 0

# for articulo, precio in carritoCompras.items():
#     total += precio
# print(f"El total a pagar es de {total}")

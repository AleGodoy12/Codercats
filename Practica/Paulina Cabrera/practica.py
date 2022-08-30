# 1. Genera una lista con los valores del 1 al 100 en una lista
# lista=[]
# for i in range(1,101):
#     lista.append(i)
# print(lista)
# # 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

# def multiplicacion():
#     num= int(input("Ingrese un numero: "))
#     tabla=[]
#     for i in range (0,10):
#         tabla.append(num*(i+1))
#     print(tabla)
# print(multiplicacion())
# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

# listaNum =[]

# while True:
#     numuser= int(input("Ingrese numeros: [0 para salir]"))
#     if numuser != 0:
#         listaNum.append(numuser)
#         listaNum.sort()
#         print(listaNum)
#     else:
#         print("Usted oprimio 0, fin del programa")
#         break
# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.
# listaNum =[]

# while True:
#     numuser= int(input("Ingrese numeros: [0 para salir]"))
#     if numuser != 0:
#         listaNum.append(numuser)
#         listaNum.sort(reverse= True)
#         print(listaNum)
#     else:
#         print("Usted oprimio 0, fin del programa")
#         break

# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
# listaNumerica= []
# while True:
#     numeros= int(input("Ingrese numeros [0 para finalizar]: "))
#     if numeros!=0:
#         listaNumerica.append(numeros)
#         print(listaNumerica)
#     else:
#         print("Ejecucion finalizada")
#         break
        

# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

# listadeterminada = [1,2,1, 2,3,7, 4,5,6,7,8,9,10]

# numB= int(input("Ingrese el numero que quiere eliminar: "))

# if numB in listadeterminada:
#     print(listadeterminada)
#     listadeterminada.remove(numB)
#     print(listadeterminada)
# else:
#     print("No es posible eliminar ya que el elemento no se encuentra en la lista")    

# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
# lista=[5,10,15,20]
# acumulador =0
# for i in lista:
#     acumulador+=i
# print(f"la suma total es ={acumulador}")
# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
## listaNueva=[]
# numerodado= int(input("Ingrese un numero"))
# def losChicos():
#     for num in listaoriginal:
#         if num<numerodado:
#             listaNueva.append(num)
#     return listaNueva
# print(losChicos())
# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
# lalista=[5,16,2,5,57,5,2]
# repeticiones=  []
# def aparece():
#     for a in lalista:
#        if lalista.count(a) >0:
#           repeticiones.append([a,lalista.count(a)])
#     return repeticiones
# print(aparece())
# 1. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
# -Agregar pasajeros a la lista de viajeros.
# -Agregar ciudades a la lista de ciudades.
# -Dado el DNI de un pasajero, ver a qué ciudad viaja.
# -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
# -Dado el DNI de un pasajero, ver a qué país viaja.
# -Dado un país, mostrar cuántos pasajeros viajan a ese país.
# -Salir del programa.

pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]

ciudades =[("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]

def agregar_viajeros():
    while True:
        nombre: input("Ingrese su nombre: ")
        dni= int(input("Ingrese su numero de dni: "))
        destino= input("Ingrese su destino: ")
        pasajeros.append((nombre,dni,destino))
         
           
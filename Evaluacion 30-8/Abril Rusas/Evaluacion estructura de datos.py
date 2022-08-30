# #Evaluacion Estructura de datos.

# # ### Se presentan 3 consignas, una por cada estructura de datos donde se busca ademas de la resolucion efectiva, un codigo lo mas escalable y limpio posible.

# # #### Al finalizar, avisar en hilo por el canal de slack, asi me acerco y de forma aleatoria me explican una de las resoluciones de los ejercicios realizados. 

# # 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.
diccionario={"Matemática":"Paula","Lengua":"Lorena","Historia":"Valeria","Geografía":"Maximiliano"}
diccionario.update({"Matemática":"Mirian","Historia":"Gustavo"})
print(diccionario)

# # 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor
numeros=[]
num=int(input("Ingrese un número [para finalizar ingrese 0]: "))
while num!=0:
    numeros.append(num)
    num=int(input("Ingrese un número [para finalizar ingrese 0]: "))
print("Usted ha finalizado")
numeros.sort()
numeros.reverse()
print(numeros)

# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
indice=int(input("Ingrese un número del 1 al 11: "))
while indice!=0:
    if indice>=1 and indice < len(meses):
        print(meses[indice])
        indice=int(input("Ingrese un número del 1 al 11 [para finalizar ingrese 0]: "))
    else:
        print("Error, debe ingresar un numero del 1 al 11")
        break
print("Programa finalizado")

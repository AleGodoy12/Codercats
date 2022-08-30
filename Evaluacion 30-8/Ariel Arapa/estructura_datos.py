# Evaluacion Estructura de datos.

### Se presentan 3 consignas, una por cada estructura de datos donde se busca ademas de la resolucion efectiva, un codigo lo mas escalable y limpio posible.

#### Al finalizar, avisar en hilo por el canal de slack, asi me acerco y de forma aleatoria me explican una de las resoluciones de los ejercicios realizados. 

# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.
materias = {"matematica": "Jose Raul", "Lengua y literatura": "Maria Ramos", "Dibujo Tecnico": "Hugo Saad", "Fisica" : "Marta Sanchez"}
nombre1 = input("Ingrese el nombre de docente de matematica: ")
nombre2 = input("Ingrese el nombre de docente de Fisica: ")

print("Lista original: ", materias)
materias.update({"matematica": nombre1, "Fisica": nombre2})
print("Lista nueva: ", materias)



# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor
listaNum = []
while True:
    num = int(input("Ingrese un numero a la lista: "))
    if num == 0:
        break
    listaNum.append(num)

listaNum.sort(reverse=True)
print(listaNum)



# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    indice = int(input("Ingrese un numero de mes: "))
    if indice > 0 and indice < len(meses) + 1:
        print("El mes es:", meses[indice - 1])
    elif indice == 0:
        print("Fin de operación.")
        break
    else:
        print("No se encuentra mes con el numero", indice, ", vuelva a intentarlo!")

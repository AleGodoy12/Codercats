#1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.


docentes={"Practicas del lenguaje":"Andrea","Matemática":"Sofía","Cs. Sociales":"Matias","Cs Naturales":"Érica","Arte":"Federico"}
docentes["Matemática"]="Mayra"
docentes["Arte"]="Morena"
print(docentes["Arte"],docentes["Matemática"])

#2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor

nro=int(input("Ingresá de a uno los nros que quieras agregar a la lista (para terminar ingresá 0) : "))
lista=[]
while nro!=0:
    lista.append(nro)
    nro=int(input("Perfecto! Ingresá otro (para terminar ingresá 0) :"))
lista.sort()
lista.reverse()
print(lista)

#3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
n=int(input("Ingresá un número, para terminar ingresá 0: "))
while n!=0:
    if n>0 and n<=len(meses):
        print(meses[n-1])
        n=int(input("Ingresá otro número: "))
    else:
        print(f"Error! El número supera el la longitud máxima({len(meses)})")
        n=int(input("Ingresá otro número: "))
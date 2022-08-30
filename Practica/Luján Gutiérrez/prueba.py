# Ejercicios Listas, tuplas y diccionarios

# 1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). 
# Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.

# 2. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla
# , muestra el contenido de esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero.

# 3. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

# 4. Crea un programa e inserte los valores del 50 al 100 en una lista
def contador ():
    for i in range(50, 101):
        print(i)
contador()

# 5. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista y la muestre por pantalla.
def asignaturas ():
    lista = []
    materias = input('ingresa una materia, para terminar ingresa 0 ')
    while materias != "0":
        lista.append(materias)
        materias = input('ingresa una materia ')
    print(lista)
asignaturas()
    
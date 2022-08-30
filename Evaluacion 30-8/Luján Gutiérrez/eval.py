# Evaluacion Estructura de datos.

#1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.
dicc= {}
def profesores ():    
    dicc = {'Python':'Tali', 'Base de datos': 'Ale', 'JS':'Gabriel'}
    print('Diccionario original' , dicc)
    dicc['Python'] = 'Ale'
    dicc['Base de datos'] = 'Tali'
    print('Diccionario actualizado',  dicc)
profesores()

#2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor
lista = []
def listaNumeros():
    numeros = input('Ingresá un número')
    while numeros != "0":
        lista.append(numeros)
        numeros = input('Ingresá un número')
    print(lista)
    lista.sort()
    lista.reverse()
    print('De mayor a menor', lista)
listaNumeros()

# #3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
numUsuario = int(input('Ingresá un numero'))
while numUsuario != 0:
    if numUsuario < len(meses):
        print(meses[numUsuario -1])
        break
    else: 
        print('Error')   
        break 


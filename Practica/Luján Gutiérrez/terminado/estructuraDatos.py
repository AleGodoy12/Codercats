1
arr = []
def lista ():
    numeros = int(input('Ingresá un número '))
    while (numeros != 0):
        arr.append(numeros)
        numeros = int(input('Ingresá un número '))
    print(arr)
lista()

def estaOno ():
    unNumero = int(input('Ingresá un numero para eliminar '))
    if (unNumero in arr):
        arr.remove(unNumero)
        print(arr)
    else:
        print('No se pudo eliminar \n')
estaOno()

def sumaElementos ():
    i=0
    suma = 0
    for i in arr:
        suma += i
        i += 1
    print(suma)
sumaElementos()

nuevoArr = []
def listaSorpresa ():
    numero = input('Ingresá un número ')
    for i in arr:
        if i < int(numero):
            nuevoArr.append(i)
    print(nuevoArr)
listaSorpresa()  

# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
# cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
# Por ejemplo, si la lista original es  la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
dicc = {}
arr = [5,16,2,5,57,5,2]
def contando ():
    
    for i in arr:
        arr.count(i)
        arr.append(i)
contando()

#3
dicc = {}
def agenda ():
    agregar = input('Quiere agregar a alguien? [SI/NO] ').upper()
    while agregar == 'SI':
        nombre = input('Ingresá el nombre')
        if nombre in dicc:
            print('No se pueden agregar nombres repetidos')
        else:
            telefono = input('Ingresá su teléfono')
            dicc[nombre] = telefono       
        agregar = input('Quiere agregar a alguien? [SI/NO] ').upper()
    print(dicc)
agenda()

# 4. Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
dicc = {}
def deCompras ():
    otroProducto = input('Querés agregar un producto? [SI/NO]').upper()
    if otroProducto == 'SI':
        while otroProducto == 'SI':
            producto = input('Ingresá el nombre de un producto')
            precio = input('Su precio')
            dicc[producto] = precio
            otroProducto = input('Querés agregar un producto? [SI/NO]').upper()
        suma = dicc.values
        print(dicc.keys)
        print(suma)
deCompras()



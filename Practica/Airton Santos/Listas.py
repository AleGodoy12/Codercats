# # Listas

# 1. Genera una lista con los valores del 1 al 100 en una lista.

i = 1
lista = []

while i < 100:
    lista.append(i)
    i += 1
print(lista)


# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
# Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50


multiplicador = int(input("Ingrese un número"))
resultado = 0 
i = 1
lista2 = []

while i <= 10:

    resultado = multiplicador * i
    lista2.append(resultado)
    i += 1
    
print(lista2)


# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.

inputUnumeros = int(input("Ingrese un número"))
lista3 = []

while inputUnumeros != 0:

    lista3.append(inputUnumeros)
    print(sorted(lista3))
    inputUnumeros = int(input("Ingrese un número"))



# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. 
# Por último, muestra los números ordenados de mayor a menor.


inputUnumeros = int(input("Ingrese un número"))
lista4 = []

while inputUnumeros != 0:

    lista4.append(inputUnumeros)
    listaOrdenada = sorted(lista4)
    print(listaOrdenada[::-1])
    inputUnumeros = int(input("Ingrese un número"))


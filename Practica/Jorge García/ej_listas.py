# 1. Genera una lista con los valores del 1 al 100 en una lista.

lista = []

for i in range(101):
    lista.append(i)
print(lista)

# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10.
#  Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Tabla del número: "))
listaMultiplicar = []
for i in range(1, 11):
    listaMultiplicar.append(i*numero)
print(listaMultiplicar)

# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese 
# un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

lista = []
num  = ""
while num != 0:
    num = int(input("Número: "))
    if(num != 0):
        lista.append(num)
lista.sort()
print(lista)

# 4. Crea un programa que pida al usuario números, genera en una lista, 
# cuando el usuario ingrese un 0 dejaremos de insertar. 
# Por último, muestra los números ordenados de mayor a menor.

lista = []
num  = ""
while num != 0:
    num = int(input("Número: "))
    if(num != 0):
        lista.append(num)
lista.sort(reverse=True)
print(lista)
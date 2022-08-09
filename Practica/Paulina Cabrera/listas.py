# Listas

# 1. Genera una lista con los valores del 1 al 100 en una lista.

from audioop import reverse


variable= []

for i in range(0, 100):
    i += 1
    variable.append(i)
    
print(variable)
    
# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

multiplicando = int(input("Quiero la tabla del: "))
multiplicador = 0
guardador = []

while (multiplicador < 10):
    multiplicador += 1
    resultado = multiplicando * multiplicador
    guardador.append(resultado)
    print(guardador)
print(guardador)
# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
listita = []
while True:
    number=int(input("Escriba los números que quiera agregar a la lista. Para finalizar ingrese 0: "))
    if (number == 0):
        break
    listita.append(number)
listita.sort()
print(listita)
# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.

listita = []
while True:
    number=int(input("Escriba los números que quiera agregar a la lista. Para finalizar ingrese 0: "))
    if (number == 0):
        break
    listita.append(number)
listita.sort(reverse=True)
print(listita)
# # Listas

# 1. Genera una lista con los valores del 1 al 100 en una lista.
lista=[]
for i in range(1,101):
    lista.append(i)
print(lista)

# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
multiplicando=int(input("Ingrese un numero: "))
multiplicador=0  
productos=[]

while (multiplicador<10):
    multiplicador += 1  
    producto = multiplicando * multiplicador
    productos.append(producto)
print(productos)

# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
lista=[]
num=int(input("Ingrese un numero: "))
while num!=0:
    lista.append(num)
    num=int(input("Ingrese un numero: "))
lista.sort()
print(lista)

# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.
lista=[]
num=int(input("Ingrese un numero: "))
while num!=0:
    lista.append(num)
    num=int(input("Ingrese un numero: "))
lista.sort()
lista.reverse()
print(lista)
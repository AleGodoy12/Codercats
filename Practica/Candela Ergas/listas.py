# 1. Genera una lista con los valores del 1 al 100 en una lista.
lista=[]
for i in range(0,100):
    lista.append(i+1)
print(lista)

# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
def mult(n):
    tabla=[]
    for i in range (0,10):
        tabla.append(n*(i+1))
    print(tabla)

mult(3)
# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

def nOrden():
    num=int(input("Inserte un número: "))
    listNum=[]
    while num!=0:
        listNum.append(num)
        num=int(input("Inserte otro: "))    
    listNum.sort()
    print(listNum)
nOrden()

# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar.  Por último, muestra los números ordenados de mayor a menor.
def mayor():
    num=int(input("Inserte un número: "))
    listNum=[]
    while num!=0:
        listNum.append(num)
        num=int(input("Inserte otro: "))    
    listNum.sort(reverse=True)
    print(listNum)
mayor()

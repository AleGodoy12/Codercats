#1
lista = []
i = 0
for i in range(0,100):
    lista.append(i)
    i += 1
    print(i)

#2
num = int(input('Ingresá un número'))
for i in range(0, 10):
    multi = num * i 
    i+=1
    print(multi)

#3
num = int(input('Ingresá un número'))
lista = []
while (num != 0):
    num = int(input('Ingresá un número'))
    lista.append(num)
lista.sort()
print(lista)

#4
lista = []
num = int(input('Ingresá un número'))
while (num != 0):
    lista.append(num)
    num = int(input('Ingresá un número'))
lista.sort(reverse=True)
print(lista)
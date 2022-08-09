# # Listas

# 1. Genera una lista con los valores del 1 al 100 en una lista.
# a = []
# for i in range(1, 101):
#     a.append(i)

# print(a)


# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
# num = int(input("Ingrese un numero: "))

# for i in range(1, 11):
#     multi = num * i
#     print(f"{num} x {i} = {multi} ")

# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
# ar = []
# while True:
#     num = int(input("Ingrese numeros: "))
#     if num == 0:
#         break   
#     ar.append(num)
# ar.sort()
# print(ar)

# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.
ar = []
while True:
    num = int(input("Ingrese numeros: "))
    if num == 0:
        break   
    ar.append(num)
ar.sort(reverse=True)
print(ar)
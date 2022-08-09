# #1
# numero = input('Ingresá un numero')
# i = 0
# def numero (num):
#     while (num != 0):
#         i += num
#         i += 1
#         return i 

#2 intento 
# digitos = []
# num = '?'
# def numero (num):
#     num = int(input('Ingresa un numero'))
#     i = 0
#     for i in num: 
#         i += 1
#         digitos.append(i)
#         suma = sum(digitos) 
#     return suma

# numero(num)

lista = []
num = int(input('Ingresá un número'))
while (num != 0):
    lista.append(num)
    num = int(input('Ingresá un número'))
lista.sort(reverse=True)
print(lista)


#1
mail = str(input('Ingresá tu mail '))
i = 0
def esValido(mail):
    for i in mail:
        if '@' in mail:
            return 'Es valido'
        else: 
            return 'Es invalido'

print(esValido(mail))


#2

num = str(input('Ingresá un número'))
def sumDigitos (num):
    for i in num:
        num = str(input('Ingresá un número'))
        if num != '0':
            suma = sum(i)
        else: 
            print('Ingresaste 0, se terminó el bucle')
            break
    return suma



# def numeros(num):
#     digitos= [int(numero) for numero in str(num)]
#     acc = 0
#     for i in digitos:
#         acc += i
#     return acc

# numUsuario = input("Ingrese un número ")
# while (numUsuario != "0"):
#     print(numeros(numUsuario))
#     numUsuario = input("Ingrese un número ")
# print("Listo")


#3
numUsuario = input("Ingrese un número ")
def numeros(num):
    digitos= [int(numero) for numero in str(num)]
    acc = 0
    for i in digitos:
        acc += i
    return acc

lista = []


while (numUsuario != "0"):
    print(numeros(numUsuario))
    numUsuario = input("Ingrese un número ")
    lista.append(eval(numUsuario))

print("Listo")


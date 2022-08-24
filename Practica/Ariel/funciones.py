# # Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"
# email = input("Ingrese su direccion de email: ")

# def validarMail(mail):
#     try:
#         if mail.index("@") >= 0:
#             mensaje = "Tu mail es valido"
#     except ValueError:
#             mensaje = "Tu mail es invalido, falta el @"
#     return mensaje

# valid = validarMail(email)
# print(valid)

# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)
a = []

def suma(numeros, array):
    sumar = 0
    digitos = [int (x) for x in str(numeros)]
    for i in digitos:
        sumar += i
    array.append(numeros)
    a = f"La suma de los digitos es: {sumar}"
    return a

import time 
while True:
    num = int(input("Ingrese numeros: "))
    if (num == 0):
        print("Cortando ejecucion...")
        time.sleep(2)
        print("Bucle finalizado!")
        break
    sumar = suma(num, a)
    print(sumar)



# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.
# a = []

# def suma(numeros, array):

#     sum = 0
#     sumar = 0
#     digitos = [int (x) for x in str(numeros)]
#     for i in digitos:
#         sumar += i
#     array.append(numeros)
#     for n in array:
#         sum += n
#     a = f"La suma de los digitos es: {sumar}"
#     b = f"La sumatoria de los numeros: {sum}"
#     return a, b

# import time 
# while True:
#     num = int(input("Ingrese numeros: "))
#     if (num == 0):
#         print("Cortando ejecucion...")
#         time.sleep(2)
#         print("Bucle finalizado!")
#         break
#     sumar = suma(num, a)
#     print(sumar)

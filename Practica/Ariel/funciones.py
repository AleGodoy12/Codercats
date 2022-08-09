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
# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.

a = []
b = []
sumatoria = 0

def suma(numeros, array):
    sum = 0
    array.append(numeros)
    for n in array:
        sum += n
    return sum

while True:
    num = int(input("Ingrese numeros: "))
    if (num == 0):
        break
    sumar = suma(num, a)
    sumatoria += sumar


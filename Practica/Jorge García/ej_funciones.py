# 1. Solicitar al usuario que ingrese su dirección email. 
# Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

def validarMail(mail):
    if('@' in mail):
        return True
    else:
        return False

correo = input("Ingresa tu mail: ")
if(validarMail(correo)):
    print("¡Tu mail es válido!")
else:
    print("Tu mail NO es válido")

# 2. Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

def sumar(num1, num2):
    suma = num1 + num2
    print(f"{num1} + {num2} = {suma}")
    return suma

num1  = ""
num2  = ""
while num1 != 0 and num2 != 0:
    num1 = int(input("Número 1 [0 para salir]: "))
    if num1 == 0: continue
    num2 = int(input("Número 2 [0 para salir]: "))
    if num2 == 0: continue
    if(num1 != 0 and num2 != 0):
        sumar(num1, num2)

# 3. Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.

def sumatoria(lista):
    if(len(lista) > 0):
        acumulador = 0
        print(lista)
        for i in lista:
            indiceSig = lista.index(i)+1
            if(indiceSig <= len(lista)-1):
                sumar(i, lista[indiceSig])
            acumulador += i
        return acumulador
    return None

num1  = ""
num2  = ""
numeros = []
while num1 != 0 and num2 != 0:
    num1 = int(input("Número 1 [0 para salir]: "))
    if num1 == 0: continue
    num2 = int(input("Número 2 [0 para salir]: "))
    if num2 == 0: continue
    sumar(num1, num2)
    numeros.append(num1)
    numeros.append(num2)
print(f'Sumatoria: {sumatoria(numeros)}')
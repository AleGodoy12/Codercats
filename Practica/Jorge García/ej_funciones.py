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

def sumarDigitos(numero):
    digitos = []
    for i in numero:
        if (i != '-'):
            digitos.append(int(i))
    return sum(digitos)

numeroStr = ""
while numeroStr != '0':
    numeroStr = input("Número [0 para salir]: ")
    if numeroStr == '0': continue
    resultado = sumarDigitos(numeroStr)
    print(f'Suma de los digitos del número {numeroStr} = {resultado}')

# 3. Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.

def sumatoria(lista):
    if(len(lista) > 0):
        return sum(lista)
    return None

numeroStr = ""
listaNumeros = []
while numeroStr != '0':
    numeroStr = input("Número [0 para salir]: ")
    if numeroStr == '0': continue
    resultado = sumarDigitos(numeroStr)
    print(f'Suma de los digitos del número {numeroStr} = {resultado}')
    listaNumeros.append(int(numeroStr))

sumaTotal = sumatoria(listaNumeros)
if(sumaTotal == None):
    print('La lista esta vacia')
else:
    print(f'Sumatoria de la lista = {sumaTotal}')
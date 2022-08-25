# # Ejercicios

import numpy as np
import time 
# 1- Generar un array aleatorio de 100 elementos. Calcular la mediana correspondiente.
# listaRandom = np.random.randint(100, size=100)
# print(listaRandom)
# media = 0
# for x in listaRandom:
#     media += x

# media = media / len(listaRandom)
# print(f"La media es: {media}")


# 2- Recordar los ejercicios con funciones para cálculo de factorial y suma de serie. Repetir ambos ejercicios (puede ser sobre el mismo código), pero ahora utilizar las nuevas operaciones aprendidas con los ndarrays.

#                              Original
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


#                              Con numpy
# def suma():
#     a = np.array([])
#     while True:
#         sum = 0  
#         sumar = 0
#         numeros = int(input("Ingrese numeros: "))
#         digitos = [x for x in str(numeros)]
#         for i in digitos:
#             sumar += int(i)
#         a = np.append(a, numeros)
#         for z in a:
#             sum += z
#         if (numeros == 0):
#             print("Cortando ejecucion...")
#             time.sleep(2)
#             print("Bucle finalizado!")
#             break
#         print(f"La suma de los digitos es: {sumar}, La sumatoria de los numeros: {sum}")
    

# suma()

#                              Original
# num = int(input("Ingrese un numero: "))
# def factorial(numero):
#     resultado, a= 1, numero
#     while a != 0:
#         resultado *= a
#         a -= 1
#     return resultado

# factorial1 = factorial(num)
# print(f"El factorial de !{num} = {factorial1}")

#                             Con numpy
listaNp = np.arange(1, 11)

def factorial(numero):
    resultado, a= 1, numero
    while a != 0:
        resultado *= a
        a -= 1
    return resultado

for x in listaNp:
    factorial1 = factorial(x)
    print(f"El factorial de !{x} = {factorial1}")
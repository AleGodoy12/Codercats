import numpy as np

# 1- Generar un array aleatorio de 100 elementos. Calcular la mediana correspondiente.

arrayNp = np.random.randint(101, size=100)
print(f'Mediana: {np.median(arrayNp)}')

# 2- Recordar los ejercicios con funciones para cálculo de factorial y suma de serie. Repetir ambos ejercicios (puede ser sobre el mismo código), pero ahora utilizar las nuevas operaciones aprendidas con los ndarrays.

#.- Ejercicio del factorial
def calcularFactorial(numero): 
    if(numero > 0):
        return np.math.factorial(numero)
    return 0

numero = int(input("Ingresa un número entero positivo: "))
print(f'Factorial = {calcularFactorial(numero)}')

#.- Ejercicio suma de serie
def sumatoria(lista):
    if(len(lista) > 0):
        return np.array(lista).sum()
    return 0

numeroStr = ""
listaNumeros = []
while True:
    numeroStr = input("Número [0 para salir]: ")
    if numeroStr == '0': break
    listaNumeros.append(int(numeroStr))
print(f'Sumatoria = {sumatoria(listaNumeros)}')
    

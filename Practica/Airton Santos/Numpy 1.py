import numpy as np

# Ejercicios

# 1- Generar un array aleatorio de 100 elementos. Calcular la mediana correspondiente.

arrAleatorio = np.random.randint(100, size=(100))
mediana = np.median(arrAleatorio)

print(mediana)
    
# 2- Recordar los ejercicios con funciones para cálculo de factorial y suma de serie. Repetir ambos ejercicios (puede ser sobre el mismo código), pero ahora utilizar las nuevas operaciones aprendidas con los ndarrays.

def factorial(numero):

    arrRango = np.array(range(1, numero + 1))
    total = 1

    for i in arrRango:
        total *= i

    print(total)

factorial(5)

def sumaSeries(num1, n):

    arrRange = np.array(range(n, n+6))
    print(arrRange)

    i = 0 
    total = 0 
    
    while i < (len(arrRange)):
        total += num1 * (n)
        n += 1 
        i += 1
    print(total)

    
sumaSeries(5,5)

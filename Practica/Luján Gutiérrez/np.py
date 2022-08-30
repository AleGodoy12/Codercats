import numpy as np

#Generar un array aleatorio de 100 elementos. Calcular la mediana correspondiente.
arr = np.arange(1,100)
mediana = np.median(arr) 
print(mediana)

# Recordar los ejercicios con funciones para cálculo de factorial y suma de serie. Repetir ambos ejercicios 
# (puede ser sobre el mismo código), pero ahora utilizar las nuevas operaciones aprendidas con los ndarrays.
print('-------------')
numero = 10
fact = np.math.factorial(numero)
print(fact)

#Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
print('-------------')
arr = np.array([0,0,0,0,0,0,0,0,0,0])
print(arr)
arr[5] = 1
print('array actualizada \n' , arr)

#Crea un objeto ndarray con elementos del 10 al 49.
print('-------------')
arr = np.arange(10,50,1)
print('vamo a contar del 10 al 49 \n', arr)

#Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.
print('-------------')
arr = np.arange(1,17,1)
matriz = arr.reshape(4,4)
print('Una matriz 4*4 \n', matriz)

#Crea una matriz, que puede completar la transposición de la posición de las coordenadas de (0,1,3) a (3,0,1). ...
print('-------------')
lista =[0,1,3]
arr = np.array(lista)
#301

#Cree una matriz bidimensional, use el índice para obtener los datos en la segunda fila, primera columna y tercera fila, segunda columna.
print('-------------')
arr = np.arange(1,17,1)
matriz = arr.reshape(4,4)
print(matriz)
donde = matriz[1,0]
print('El elemento que está en la segunda fila, primera columna es:', donde)
donde2 = matriz[2,1]
print('El elemento que está en la tercera fila, segunda columna es:', donde2)

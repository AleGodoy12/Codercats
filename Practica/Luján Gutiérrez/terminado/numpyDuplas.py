import numpy as np
# 1 Crear una matriz 3x3 con valores del 0 al 8
arr = np.arange(0,9)
matriz = arr.reshape(3,3)
print('Ejercicio n°1 \n', matriz)

#2 Crear una matriz de identidad de 3x3
arr = np.identity(3)
print('Ejercicio n°2 \n', arr)

#3 Utilizar numpy para geneara un numero aleatorio entre 0 y 1
num = np.random.rand()
print('Ejercicio n°3 \n', num)

#4 Utilizar numpy para generar un arreglo de 25 numeros aleatorioas con una   distribucion normal
num = np.random.rand(25)
print('Ejercicio n°4 \n', num)

#5 Crear la siguiente matriz
arr = np.arange(1,101)
matriz = arr.reshape(10,10) /100
print('Ejercicio n°5 \n', matriz)

#6 Crear un arreglo de 20 valores lineales entre 0 y 1
# Output:
# array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
#        [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
#        [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
#        [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
#        [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
#        [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
#        [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
#        [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
#        [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
#        [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]]) 
arr = np.linspace(0, 1, 20)
print('Ejercicio n°6 \n', arr)

#7
apellido = ('ARodriguez', 'COrtega', 'ARodriguez')
nombre = ('Julian', 'Brishito', 'Gastón')
indice = np.lexsort((apellido, nombre)) #solo funciona con dos o más matrices
print(indice)

#lexsort ordena alfabeticamente
#la segunda matriz le da directrices para ordenar la primera

print('----')
print('OUTPUT [1 2 0]')
print('----')

apellido = ('ab', 'cd', 'ab')
nombre = ('cc', 'aa', 'dd')
indice = np.lexsort((apellido, nombre))
print(indice)

print('----')

apellidos =    ('Zota', 'Zota', 'Zota')
nombre = ('Andres', 'Carla', 'Gustavo')
print(np.lexsort((nombre, apellidos))) #siempre empieza con el segundo parametro independientemente de como lo tenemos arriba

print(np.lexsort((apellidos, nombre)))

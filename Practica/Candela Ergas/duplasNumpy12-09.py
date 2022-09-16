import numpy as np
# 1. Crear una matriz 3x3 con valores del 0 al 8

# <!-- OutPut:
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]]) -->

arr1= np.arange(9).reshape(3,3)
print(arr1)

# 2. Crear una matriz de identidad de 3x3

# <!-- Output:
# array([[ 1.,  0.,  0.],
#        [ 0.,  1.,  0.],
#        [ 0.,  0.,  1.]]) -->

mi= np.identity(3)
print(mi)

# 3. Utilizar numpy para geneara un numero aleatorio entre 0 y 1
 
random= np.random.rand()
print(random)

# 4. Utilizar numpy para generar un arreglo de 25 numeros aleatorioas con una   distribucion normal

random1= np.random.randn(5,5)
print(random1)

# 5. Crear la siguiente matriz

# <!-- Output:
# array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
#        [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
#        [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
#        [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
#        [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
#        [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
#        [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
#        [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
#        [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
#        [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]]) -->

arr = np.arange (0.01, 1.01, 0.01).reshape(10,10)
print(arr)

# # matriz1= np.linspace(0,1,100).round(2) PREGUNTAR
# # print(matriz1)

# 6. Crear un arreglo de 20 valores lineales entre 0 y 1

# <!-- Output:array([ 0.        ,  0.05263158,  0.10526316,  0.15789474,  0.21052632,
#         0.26315789,  0.31578947,  0.36842105,  0.42105263,  0.47368421,
#         0.52631579,  0.57894737,  0.63157895,  0.68421053,  0.73684211,
#         0.78947368,  0.84210526,  0.89473684,  0.94736842,  1.        ]) -->

matriz2= np.linspace(0,1,20)
print(matriz2)

# 7. Generar pares de apellidos y nombres y devolver sus índices. (primero por apellido, luego por nombre).


# <!-- OUTPUT [1 2 0] -->

nombre = ( "Cesar", "Ana", "Gabriel")

apellido = ("Sanchez", "Cardenas", "Gonzalez")

print (np.lexsort((nombre, apellido)))
# # Ejercicios para realizar en equipo con las duplas asignadas. Cada equipo va a explicar un ejercicio de forma aleatoria en la puesta en comun.
import numpy as np
# 1. Crear una matriz 3x3 con valores del 0 al 8
matriz=np.arange(0,9).reshape(3,3)
print("Matriz de 3x3 del 0 al 8\n",matriz)

# 2. Crear una matriz de identidad de 3x3
identidad=np.identity(3)
print("Matriz identidad de orden 3\n",identidad)

# 3. Utilizar numpy para geneara un numero aleatorio entre 0 y 1
num=np.random.random()
print("Numero aleatorio entre 0 y 1:",num)

# 4. Utilizar numpy para generar un arreglo de 25 numeros aleatorioas con una distribucion normal
numeros=np.random.normal(0,2,25)
print("25 numeros aleatorios con una distribucion normal\n",numeros)
# <!-- OutPut:
# array([-2.02210433,  2.13979668, -1.2894587 , -0.2519908 ,  0.18878965,
#        -2.5725129 , -0.397411  , -0.29968372,  1.61758908, -0.21690755,
#        -1.70163065,  1.29327542,  0.93088122, -2.06747839,  0.45213864,
#         0.33541953, -0.52377853,  1.93545321,  0.82036754,  1.36417092,
#         0.02392979,  0.29879047, -1.15224828,  0.19279692, -0.46335562]) -->

# 5. Crear la siguiente matriz
matriz=np.arange(0.01,1.01,0.01).reshape(10,10)
print(matriz)

# 6. Crear un arreglo de 20 valores lineales entre 0 y 1
matriz=np.arange(0,1.05,0.05263158)
print(matriz)
# <!-- Output:array([ 0.        ,  0.05263158,  0.10526316,  0.15789474,  0.21052632,
#         0.26315789,  0.31578947,  0.36842105,  0.42105263,  0.47368421,
#         0.52631579,  0.57894737,  0.63157895,  0.68421053,  0.73684211,
#         0.78947368,  0.84210526,  0.89473684,  0.94736842,  1.        ]) -->

# 7. Generar pares de apellidos y nombres y devolver sus índices. (primero por apellido, luego por nombre).
surnames =    ('Gramajo','Rusas','Gramajo')
first_names = ('Lucas','Abril','Agustin')
print (np.lexsort((surnames,first_names)))
# <!-- OUTPUT [1 2 0] -->
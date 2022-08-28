# ## Ejercicios
import numpy as np
# * 1, Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
# arr0 = np.zeros(10)
# print("Array inicial", arr0)
# arr0[4] = 1
# print("Array nuevo", arr0)


# # * 2, Crea un objeto ndarray con elementos del 10 al 49.
# arr1 = np.arange(10, 49)
# print(arr1)


# # * 3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.
# arr2 = np.arange(16)
# print(arr2.reshape(4, 4))


# * 4, Crea una matriz, que puede completar la transposición de la posición de las coordenadas de (0,1,3) a (3,0,1). ...
x = np.ones((0, 1, 3))
a = np.transpose(x, (2, 0, 1)).shape
print(a)


# * 5, Cree una matriz bidimensional, use el índice para obtener los datos en la segunda fila, primera columna y tercera fila, segunda columna.
# arr5 = np.arange(16).reshape(4, 4)
# print(arr5)
# arr6 = arr5[1,...] #da la segunda fila
# print(arr6)
# arr7 = arr5[...,0] #da primera columna
# print(arr7)
# arr8 = arr5[2,...] #da la tercera fila
# print(arr8)
# arr9 = arr5[...,1] #da segunda columna
# print(arr9)

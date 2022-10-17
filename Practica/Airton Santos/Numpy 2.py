import numpy as np


# ## Ejercicios

# * 1, Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.

newArr = np.zeros(10)
newArr[4] = 1 
print(newArr)

# * 2, Crea un objeto ndarray con elementos del 10 al 49.

newArr2 = np.arange(10,49,1)
print(newArr2)



# * 3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.

newArr3 = np.arange(1,17,1)
arr = newArr3.reshape(4,4)
print(type(newArr))

# * 4, Crea una matriz, que puede completar la transposición de la posición de las coordenadas de (0,1,3) a (3,0,1). ...

x = np.ones((0, 1, 3))
a = np.transpose(x, (2, 0, 1)).shape
print(a) 

# * 5, Cree una matriz bidimensional, use el índice para obtener los datos en la segunda fila, primera columna y tercera fila, segunda columna. 

newArr4 = np.arange(10,19,1)
arr2 = newArr4.reshape(3,3)
segundaFila = arr2[1,:]
primeraCol = arr2[:,0]
tercerFila = arr2[2,:]
segundaCol = arr2[:,1]



 
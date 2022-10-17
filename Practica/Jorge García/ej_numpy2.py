import numpy as np

# * 1, Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.

vector = np.zeros(10, dtype=int)
vector[4] = 1
print(vector)

# * 2, Crea un objeto ndarray con elementos del 10 al 49.

vector = np.arange(10, 50)
print(vector)

# * 3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.

matriz = np.arange(1, 17).reshape(4, 4)
print(matriz)

# * 4, Crea una matriz, que puede completar la transposición de la posición de las coordenadas de (0,1,3) a (3,0,1). ...

vector1 = np.array((0,1,3))
vector2 = np.array((3,0,1))
matriz = np.concatenate([vector1, vector2]).reshape(2, 3)
matriz_t = np.transpose(matriz)
print(matriz_t)

# * 5, Cree una matriz bidimensional, use el índice para obtener los datos en la segunda fila, primera columna y tercera fila, segunda columna.

matriz = np.arange(1, 7).reshape(3, 2)
print(matriz) 

numero_21 = matriz[1, 0]
numero_32 = matriz[2, 1]
print(f'Segunda fila, primera columna: {numero_21}') 
print(f'Tercera fila, segunda columna: {numero_32}') 
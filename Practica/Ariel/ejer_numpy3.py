# # Numpy 
import numpy as np

# 1. Cree una matriz de formas (3, 2) y complétela con muestras aleatorias de una distribución uniforme sobre [0, 1).
# <!-- 
# # OUTPUT <!-- #array([[ 0.13879034,  0.71300174],
#            [ 0.08121322,  0.00393554],
#           [ 0.02349471,  0.56677474]]) --> 

# arr = np.random.random(6).reshape(3, 2)
# print(arr)



# 2. Cree una matriz de formas (1000, 1000) y complétela con muestras aleatorias de una distribución normal estándar. Y verifique que la media y la desviación estándar estén lo suficientemente cerca de 0 y 1 respectivamente.

# <!-- OUTPUT -0.00110028519551
# 0.999683483393 -->
# matriz = np.random.normal(0, 1, (1000, 1000))
# media = matriz.mean() #mean() se utiliza para calcular la media aritmética a lo largo del eje especificado.
# desvio_estandar = np.std(matriz)  #std() calcula la desviación estándar de el array dada a lo largo del eje especificado.
# print(f'Media: {media}')
# print(f'Desvío estándar: {desvio_estandar}')



# 3. Cree una matriz de formas (3, 2) y complétela con números enteros aleatorios que van desde 0 a 3 (inclusive) de una distribución uniforme discreta.
# <!-- OUTPUT array([[1, 3],
#        [3, 0],
#        [0, 0]]) -->
# arr3 = np.random.randint(4, size=6).reshape(3, 2)
# print(arr3)



# 4. Ordenar x a lo largo del segundo eje
# arr = [1, 3, 5, 6]
# arr1 = [2, 3, 2, 2]

# arr2 = np.concatenate((arr, arr1)).reshape(2, 4)
# print(arr2)

# 5. Generar pares de apellidos y nombres y devolver sus índices. (primero por apellido, luego por nombre).

# <!-- OUTPUT [1 2 0] -->

# 6. Cree una matriz tal que su quinto elemento sea el mismo que el elemento de x ordenado, y divida otros elementos por su valor.
x = np.array([5, 1, 6, 3, 9, 8, 2, 7, 4, 0])
x_ordenado = np.sort(x)
a = np.arange(10).reshape(5, 2)
print(x_ordenado,"\n", a)

division = np.arange(0, 100, 10)
division = division / x_ordenado[5]
print(division)
# <!-- x = [5 1 6 3 9 8 2 7 4 0]

# Check the fifth element of this new array is 5, the first four elements are all smaller than 5, and 6th through the end are bigger than 5
# [2 0 4 3 1 5 8 7 6 9] -->
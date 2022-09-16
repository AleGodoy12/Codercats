import numpy as np

# 1. Cree una matriz de formas (3, 2) y complétela con muestras aleatorias de una distribución uniforme sobre [0, 1).
# <!-- 
# # OUTPUT <!--
# #array([[ 0.13879034,  0.71300174],
#            [ 0.08121322,  0.00393554],
#           [ 0.02349471,  0.56677474]]) --> 

print("\nEjercicio 1")
matriz = np.random.uniform(0.0, 1, (3,2))
print(f'Matriz de una distribución uniforme:\n{matriz}')

# 2. Cree una matriz de formas (1000, 1000) y complétela con muestras aleatorias de una distribución normal estándar. Y verifique que la media y la desviación estándar estén lo suficientemente cerca de 0 y 1 respectivamente.

# <!-- OUTPUT -
# 0.00110028519551
# 0.999683483393 -->

# Distribución normal estádar -> Media = 0 y desviación típica = 1

print("\nEjercicio 2")
matriz = np.random.normal(0, 1, (1000, 1000))
media = matriz.mean()
desvio_estandar = np.std(matriz)
print(f'Media: {media}')
print(f'Desvío estándar: {desvio_estandar}')

# 3. Cree una matriz de formas (3, 2) y complétela con números enteros aleatorios que van desde 0 a 3 (inclusive) de una distribución uniforme discreta.

# <!-- OUTPUT 
# array([[1, 3],
#        [3, 0],
#        [0, 0]]) -->

print("\nEjercicio 3")
matriz_4 = np.random.randint(0, 4, (3,2))
print(matriz_4)

# 4. Ordenar x a lo largo del segundo eje

print("\nEjercicio 4")
matriz_4[:,0].sort()
matriz_4[:,1].sort()
print(matriz_4)

# 5. Generar pares de apellidos y nombres y devolver sus índices. (primero por apellido, luego por nombre).

# <!-- OUTPUT [1 2 0] -->

print("\nEjercicio 5")
apellidos = ('Zeta', 'Arapa', 'Diaz')
nombre = ('Andres', 'Carla', 'Gustavo')
print("\nEjercicio 5:", np.lexsort((nombre, apellidos)), "\n")

# 6. Cree una matriz tal que su quinto elemento sea el mismo que el elemento de x ordenado, y divida otros elementos por su valor.

# <!-- x = [5 1 6 3 9 8 2 7 4 0]

# Check the fifth element of this new array is 5, the first four elements are all smaller than 5, and 6th through the end are bigger than 5
# [2 0 4 3 1 5 8 7 6 9] -->

print("\nEjercicio 6")
x = np.array([5, 1, 6, 3, 9, 8, 2, 7, 4, 0])
x.sort()
nuevoArray = np.array([], dtype=float)
quintoElemento = x[5]
print(x)
for i in range(len(x)):
    if(i != 5):
        nuevoArray = np.append(nuevoArray, i/quintoElemento)
print(nuevoArray)

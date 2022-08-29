#Numpy 3

#1. Cree una matriz de formas (3, 2) y complétela con muestras aleatorias de una distribución uniforme sobre [0, 1).
import numpy as np
matriz=np.random.rand(3,2)
print(matriz)

# 2. Cree una matriz de formas (1000, 1000) y complétela con muestras aleatorias de una distribución normal estándar. Y verifique que la media y la desviación estándar estén lo suficientemente cerca de 0 y 1 respectivamente.
matriz=np.random.randn(1000,1000)
media=np.median(matriz)
desviacion=np.std(matriz)
print("La media es",media,"\nLa desviación es: ",desviacion)

# 3. Cree una matriz de formas (3, 2) y complétela con números enteros aleatorios que van desde 0 a 3 (inclusive) de una distribución uniforme discreta.
matriz=np.random.randint(0,4,size=(3,2))
print(matriz)

# 4. Ordenar x a lo largo del segundo eje


# 5. Generar pares de apellidos y nombres y devolver sus índices. (primero por apellido, luego por nombre).

# <!-- OUTPUT [1 2 0] -->

# 6. Cree una matriz tal que su quinto elemento sea el mismo que el elemento de x ordenado, y divida otros elementos por su valor.

# <!-- x = [5 1 6 3 9 8 2 7 4 0]

#7. Verifique que el quinto elemento de esta nueva matriz sea 5, los primeros cuatro elementos son todos menores que 5, y desde el sexto hasta el final son mayores que 5
# [2 0 4 3 1 5 8 7 6 9] -->
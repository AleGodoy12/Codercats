
# ## Ejercicios
import numpy as np

# * 1, Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
Np_ceros = np.zeros(10)
print("Matriz de ceros: \n",Np_ceros,"\n")

# * 2, Crea un objeto ndarray con elementos del 10 al 49.
Np_rango = np.arange(10,50)
print("Matriz de 10 al 49: \n",Np_rango,"\n")

# * 3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.
Np_random_dimensiones = np.random.randint(10, size=(4, 4))
print("Matriz de 4x4: \n",Np_random_dimensiones,"\n")

# * 4, Crea una matriz, que puede completar la transposición de la posición de las coordenadas de (0,1,3) a (3,0,1). ...
x = np.ones((0, 1, 3))
a = np.transpose(x, (2, 0, 1)).shape
print("Matriz transpuesta: \n",a,"\n") 

# * 5, Cree una matriz bidimensional, use el índice para obtener los datos en la segunda fila, primera columna y tercera fila, segunda columna.
matriz=np.array([[00,11,22], [33, 44,55], [66, 77,88]])  #Preguntar por que no acepa 01 o 02
n1=matriz[1,0]
n2=matriz[2,1]
print("Extraer elementos de una matriz \n",matriz,"\nElemento1: ",n1," Elemento2: ",n2)
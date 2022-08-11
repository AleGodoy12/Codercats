# Numpy 🐍

#### Es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.

#### Incorpora una nueva clase de objetos llamados arrays que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.

## La clase de objetos array

#### Un array es una estructura de datos de un mismo tipo organizada en forma de tabla o cuadrícula de distintas dimensiones.

#### Las dimensiones de un array también se conocen como ejes.
![Numpy](/imagenes/NUMPY.png)

## Creación de arrays
Para crear un array se utiliza la siguiente función de NumPy

1. np.array(lista) : Crea un array a partir de la lista o tupla lista y devuelve una referencia a él. El número de dimensiones del array dependerá de las listas o tuplas anidadas en lista:

2. Para una lista de valores se crea un array de una dimensión, también conocido como vector.

3. Para una lista de listas de valores se crea un array de dos dimensiones, también conocido como matriz.

4. Para una lista de listas de listas de valores se crea un array de tres dimensiones, también conocido como cubo.

#### Y así sucesivamente. No hay límite en el número de dimensiones del array más allá de la memoria disponible en el sistema.

#### 🚨 Los elementos de la lista o tupla deben ser del mismo tipo 🚨

![numpy](/imagenes/numpy1.png)

## Otras funciones útiles que permiten generar arrays son:

1. np.empty(dimensiones) : Crea y devuelve una referencia a un array vacío con las dimensiones especificadas en la tupla dimensiones.

2. np.zeros(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos ceros.

3. np.ones(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos unos.

4. np.full(dimensiones, valor) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos valor.

5. np.identity(n) : Crea y devuelve una referencia a la matriz identidad de dimensión n.

6. np.arange(inicio, fin, salto) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia desde inicio hasta fin tomando valores cada salto.

7. np.linspace(inicio, fin, n) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.

8. np.random.random(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son aleatorios.

![numpy](/imagenes/numpy2.png)

## Atributos de un array
#### Existen varios atributos y funciones que describen las características de un array.

1. a.ndim : Devuelve el número de dimensiones del array a.

2. a.shape : Devuelve una tupla con las dimensiones del array a.

3. a.size : Devuelve el número de elementos del array a.

4. a.dtype: Devuelve el tipo de datos de los elementos del array a.

### Acceso a los elementos de un array

#### Para acceder a los elementos contenidos en un array se usan índices al igual que para acceder a los elementos de una lista, pero indicando los índices de cada dimensión separados por comas.

#### Al igual que para listas, los índices de cada dimensión comienzan en 0.

#### También es posible obtener subarrays con el operador dos puntos : indicando el índice inicial y el siguiente al final para cada dimensión, de nuevo separados por comas.

![numpy](/imagenes/numpy3.png)

## Filtrado de elementos de un array

#### Una característica muy útil de los arrays es que es muy fácil obtener otro array con los elementos que cumplen una condición.

1. a[condicion] : Devuelve una lista con los elementos del array a que cumplen la condición condicion.

![numpy](/imagenes/numpy4.png)

## Operaciones matemáticas con arrays
#### Existen dos formas de realizar operaciones matemáticas con arrays: a nivel de elemento y a nivel de array.

#### Las operaciones a nivel de elemento operan los elementos que ocupan la misma posición en dos arrays. Se necesitan, por tanto, dos arrays con las mismas dimensiones y el resultado es una array de la misma dimensión.

#### Los operadores mamemáticos "+, -, *, /, %, **" se utilizan para la realizar suma, resta, producto, cociente, resto y potencia a nivel de elemento.

![numpy](/imagenes/numpy5.png)

## Álgebra matricial

#### Numpy incorpora funciones para realizar las principales operaciones algebraicas con vectores y matrices. La mayoría de los métodos algebráicos se agrupan en el submódulo linalg.

### Producto escalar de dos vectores

#### Para realizar el producto escalar de dos vectores se utiliza el operador @ o el siguiente método:

1. u.dot(v): Devuelve el producto escalar de los vectores u y v.

![numpy](/imagenes/numpy6.png)

## Módulo de un vector

#### Para calcular el módulo de un vector se utiliza el siguiente método:

1. norm(v): Devuelve el módulo del vector v

![numpy](/imagenes/numpy7.png)

## Producto de dos matrices
#### Para realizar el producto matricial se utiliza el mismo operador @ y método que para el producto escalar de vectores:

1. a.dot(b) : Devuelve el producto matricial de las matrices a y b siempre y cuando sus dimensiones sean compatibles.
![numpy](/imagenes/numpy8.png)

## Matriz traspuesta
#### Para trasponer una matriz se utiliza el método

1. a.T : Devuelve la matriz traspuesta de la matriz a.

![numpy](/imagenes/numpy9.png)

## Traza de una matriz
#### La traza de una matriz cuadrada se calcula con el siguiente método:

1. a.trace() : Devuelve la traza (suma de la diagonal principal) de la matriz cuadrada a.
![numpy](/imagenes/numpy10.png)

## Determinante de una matriz
#### El determinante de una matriz cuadrada se calcula con la siguiente función:

1. det(a) : Devuelve el determinante de la matriz cuadrada a.

![numpy](/imagenes/numpy11.png)

## Matriz inversa
La inversa de una matriz se calcula con la siguiente función:

1. inv(a) : Devuelve la matriz inversa de la matriz cuadrada a.

![numpy](/imagenes/numpy12.png)

## Autovalores de una matriz

#### Los autovalores de una matriz cuadrada se calculan con la siguiente función:

1. eigvals(a) : Devuelve los autovalores de la matriz cuadrada a.

![numpy](/imagenes/numpy13.png)

## Autovectores de una matriz

#### Los autovectores de una matriz cuadrada se calculan con la siguiente función:

1. eig(a) : Devuelve los autovalores y los autovectores asociados de la matriz cuadrada a.

![numpy](/imagenes/numpy14.png)

## Solución de un sistema de ecuaciones

#### Para resolver un sistema de ecuaciones lineales se utiliza la función siguiente:

1. solve(a, b) : Devuelve la solución del sistema de ecuaciones lineales con los coeficientes de la matriz a y los términos independientes de la matriz b.

![numpy](/imagenes/numpy15.png)
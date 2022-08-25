# Estructuras de datos. Arrays 

## Estructuras de Datos

Habitualmente, cuando trabajamos en Python con datos orientados a Data Science, vemos que estos vienen en distintos formatos o tipos de datos. Estos conjuntos de datos están organizados de una determinada manera, y gracias a ello podemos acceder a estos datos, operar con ellos, mostrarlos, y en general, manipularlos. Tal como vimos en la clase pasada, hablaremos aquí de estructuras de datos . No pensemos aquí solamente en datos que podríamos ver, por ejemplo, en una planilla. Este análisis puede extenderse a datos de otras clases, como por ejemplo archivos de audio, o imágenes. Estos tipos diversos de datos tienen que ser transformados a números para poder ser interpretados por los algoritmos. 

Por otra parte, para trabajar con estructuras de datos es necesario realizar operaciones que son habituales para este tipo de trabajo. Python ya cuenta con una serie de librerías especializadas para realizar esos trabajos. En esta clase y en la siguiente veremos los dos paquetes principales: NumPy (Numerical Python) y Pandas. Éstos paquetes proveen funciones avanzadas para trabajar con conjuntos de datos de tamaños diversos. De alguna forma, es similar a trabajar con listas, tal como vimos en la clase anterior, pero en estos casos el almacenamiento es más eficiente, y funciona muy bien con conjuntos de datos grandes.

## Arrays

Recordemos de la Clase 02 que en Python existen varios tipos de estructuras de datos, tales como list, tuple, dict y set. Cada una de estas estructuras contaba con alguna características particulares. La realidad es que habitualmente estas características no alcanzan para cubrir las necesidades del data scientist. 

A continuación extenderemos la aplicación de estos tipos de estructura de datos, agregando el tipo de dato array. 

Comparado con el tipo list, ambos tipos de datos sirven para guardar conjuntos de datos ordenados en memoria. No obstante, tienen algunas diferencias. Mientras que el tipo de dato list puede guardar datos de diferentes tipos, el tipo de dato array guarda datos de un único tipo. Esto le permite ser más eficiente, especialmente al trabajar con conjuntos de datos grandes. Además, para definir un dato de tipo array, debemos importar previamente el módulo array. Veamos su aplicación en código:

L = list(range(10))
L # Muestra una lista de 10 elementos
import array as arr #Necesitamos importar el módulo array para crear arrays
A = arr.array("i",range(10))
A # Muestra un array de 10 elementos


#NumPy y ndarrays. Creación de ndarrays 

¿Cómo lograr una mejora en el uso de estas estructuras? El paquete NumPy nos da la respuesta. NumPy define un nuevo tipo de dato denominado ndarray, que funciona como un array con vitaminas. Comencemos creando una estructura de este tipo:

import numpy as np # importamos la librería NumPy
Npa = np.array(range(10)) # creamos un ndarray de 10 elementos
Npa

import numpy as np # importamos la librería NumPy
Npa = np.array(range(10)) # creamos un ndarray de 10 elementos
Npa


Np_cero = np.zeros(10) # Ndarray de ceros
Np_cero_int = np.zeros(10, dtype=int) # Ndarray de ceros, pero especificando que sean enteros
Np_uno = np.ones(10) # Ndarray de unos
print(Np_cero, Np_cero_int, Np_uno)
Np_relleno = np.full(10,256) # Rellenar un array de 10 elementos con el número 256
Np_relleno_dimensiones = np.full((2,3),256) # Armar una matriz de 2 filas por 3 columnas y rellenarla con el número 256
print(Np_relleno)
print(Np_relleno_dimensiones)
Np_rango = np.arange(10) # Armar de forma compacta un array con números ordenados
Np_random_dimensiones = np.random.randint(10, size=(3, 4))  # Array random de 3 filas por 4 columnas
print(Np_random_dimensiones)

### De esta manera podemos crear arrays en NumPy

# Tipos de datos y atributos de arrays 
Tipos de datos
Los objetos de tipo ndarray pueden ser de un solo tipo. Como vimos anteriormente, podemos dejar el tipo vacío, con lo cual Python decide el tipo basándose en los elementos ingresados; o bien, podemos especificar el tipo, por ejemplo cuando sabemos a priori qué tipo de datos contendrá el ndarray, de tal forma de hacer más eficiente el uso de la memoria.
Para especificar el tipo de dato en la creación del ndarray, podemos consultar los tipos de la lista oficial publicada en este link: https://numpy.org/devdocs/user/basics.types.html 
Atributos
Al ser objetos de Python, los ndarrays tienen atributos. Estos atributos se ocupan de tomar registro del tamaño, forma, consumo de memoria y tipo de datos del ndarray.

print(Np_cero.ndim) # Vector de una dimensión
print(Np_relleno_dimensiones.ndim) # Matriz de 2 dimensiones (filas y columnas)
print(Np_relleno_dimensiones.shape) # 2 filas por 3 columnas
print(Np_relleno_dimensiones.size) # 6 elementos en total
print(Np_cero.dtype) # Punto flotante
print(Np_cero_int.dtype) # Enteros
print(Np_cero.itemsize) # Tamaño de cada elemento
print(Np_cero.nbytes) # Tamaño total del array
print(Np_cero_int.nbytes) # Los enteros ocupan menos que los elementos de punto flotante

## Indexado y acceso 
Acceso a elementos
Anteriormente dijimos que los arrays y ndarrays, al igual que las estructuras de tipo list, contienen datos ordenados. Esto significa que el orden de cada elemento es siempre el mismo, con lo que podemos referirnos a un elemento (o referenciarlo) a partir de su índice o número de posición. Como particularidad, en Python los índices comienzan desde el número 0. Con lo cual, un conjunto de 10 elementos tendrá índices desde el 0 hasta el 9. Veamos un ejemplo:


rango = range(1,11) # La función range incluye al primer número y excluye al último
Np_diez_numeros = np.array(rango) # Crear un ndarray que contenga al rango generado
print(Np_diez_numeros)
print(Np_diez_numeros[0]) # Primer elemento
print(Np_diez_numeros[4]) # Quinto elemento
print(Np_diez_numeros[-1]) # Cuento en reversa, comenzando por el -1 (último elemento)
print(Np_diez_numeros[-2]) # Penúltimo elemento
print(Np_random_dimensiones)
print(Np_random_dimensiones[2,1]) #Tercera fila, segunda columna

## Acceso a subarrays
En Python podemos “recortar” porciones en conjuntos de datos usando la operación de slice. Para ello usamos la siguiente notación: objeto[desde:hasta:tamaño_de_paso]. Por defecto los valores se recorren desde 0 hasta el tamaño del objeto, de a un paso (de a un elemento). Veamos algunos ejemplos a continuación:

print(Np_diez_numeros[:4]) # Primeros cuatro elementos
print(Np_diez_numeros[3:]) # Desde el cuarto elemento hasta el final
print(Np_diez_numeros[4:7]) # Ojo! Desde el quinto elemento hasta el séptimo 
print(Np_diez_numeros[::2]) # Desde el primer elemento, saltando de a dos
print(Np_diez_numeros[1::2]) # Desde el segundo elemento, saltando de a dos
print(Np_diez_numeros[::-2]) # Si el step es negativo, camino hacia atrás

En el caso de contar con más de una dimensión, accedemos en forma ordenada a cada dimensión de la forma objeto[dimensión_1,dimensión_2,...]. En cada dimensión podemos hacer un slice de la misma forma que lo hacíamos anteriormente.

print(Np_random_dimensiones[2,]) # Tercera fila, todas las columnas
print(Np_random_dimensiones[:2,:2]) # Subconjunto de primeras dos filas y primeras dos columnas
print(Np_random_dimensiones[2,3]) # Tercera fila, cuarta columna

## Operaciones básicas: reshape, concatenación, splitting 
Existen muchas operaciones para poder explotar al máximo el potencial que brinda NumPy. Podemos organizar las principales operaciones en tres grandes grupos: operaciones básicas, agregaciones y operaciones vectorizadas. Existen varios tipos más de operaciones, pero aquí veremos las básicas que permitan introducirnos en el mundo del Data Science.

## Reshape
Hasta ahora, no vimos una manera rápida de organizar elementos en un array de varias dimensiones. Supongamos por ejemplo que queremos rellenar un tablero de ajedrez (de 8 x 8 casilleros) con números, y tenemos a mano la función range() que nos permite generar los números sin necesidad de escribirlos a mano.
Si tratamos de hacer un tablero de ajedrez relleno de ceros, o de cualquier número fijo, con lo que conocemos hasta ahora es posible hacerlo fácilmente.

Ajedrez_ceros = np.zeros((8,8))
print(Ajedrez_ceros)
Ajedrez_num = np.full((8,8),35)
print(Ajedrez_num)
En cambio, si queremos rellenarlo con números consecutivos del 1 al 64, nos dará un error.
rango_ajedrez = range(1,65)
Ajedrez = np.array((8,8),rango_ajedrez) # Esto no funciona


Para solucionar esta situación y similares, NumPy define una operación denominada reshaping. Básicamente, tomamos un ndarray como entrada, y le “cambiamos la forma”, en términos de dimensiones. Veamos algunos ejemplos:

Ajedrez_64 = np.arange(1,65) # Una array de números de 1 a 64 
print(Ajedrez_64)
Ajedrez_64 = np.arange(1,65).reshape(8,8) # Organizarlo en 8 x 8
print(Ajedrez_64)
Ajedrez_64 = Ajedrez_64.reshape(8,8) # Equivalente al comando anterior
print(Ajedrez_64)

## Concatenación     *** chequear 
Para “enganchar” o concatenar dos o más arrays, utilizamos las funciones concatenate y vstack / hstack. Veamos algunos ejemplos:
Array_1 = np.random.randint(10,size=5)
Array_2 = np.random.randint(10,size=5)
print(Array_1, Array_2) # Dos arrays de 5 elementos, con números aleatorios del 0 al 9
Arrays_concatenados = np.concatenate([Array_1, Array_2]) # Un array que contiene los 10 números concatenados
print(Arrays_concatenados)
Si queremos combinar los arrays en forma explícita de manera horizontal o vertical, usaremos las funciones vstack y hstack
<br>
Array_1 = np.random.randint(10,size=5)<br>
Array_2 = np.random.randint(10,size=5)<br>
print(Array_1, Array_2) # Dos arrays de 5 elementos, con números aleatorios del 0 al 9<br>
Arrays_concatenados = np.concatenate([Array_1, Array_2]) # Un array que contiene los 10 números concatenados <br>
print(Arrays_concatenados)
Array_extra = np.array([[10],[20]]) # Un array de dos dimensiones (vertical) con los números 10 y 20
print(Array_extra)
Array_apilados_v_h = np.hstack([Array_extra,Array_apilados_v]) # Concatenar el array vertical con el array apilado
print(Array_apilados_v_h)
print(np.shape(Array_apilados_v_h)) # ¿Cuántas filas y columnas tiene?

De esta forma podemos combinar arrays.

## Splitting
Por otra parte, podemos “partir” los arrays utilizando las funciones split, hsplit y vsplit. Estas funciones reciben como argumento el array a “partir” y una lista con los puntos de corte. Podemos pensar los puntos de corte como los “huecos” existentes entre los elementos del array. Veamos los siguientes ejemplos:

Array_partido = np.split(Arrays_concatenados,[2]) # Parte el array entre el segundo y tercer elemento
print(Array_partido)
Array_partido_2 = np.split(Arrays_concatenados,[2,8]) # Parte el array entre el segundo y tercero, y entre el octavo y noveno elemento
print(Array_partido_2)
Parte_1, Parte_2, Parte_3 = Array_partido_2 # Guarda cada elemento en una variable. Muy útil
print(Parte_1, Parte_2, Parte_3)
Ajedrez_partido_1 = np.hsplit(Ajedrez_64,[4]) # Parte el tablero de ajedrez por la mitad, de forma vertical
print(Ajedrez_partido_1)
Ajedrez_partido_2 = np.vsplit(Ajedrez_64,[4]) # Parte el tablero de ajedrez por la mitad, de forma horizontal
print(Ajedrez_partido_2)
De esta manera podemos trabajar con operaciones básicas sobre arrays.

## Agregaciones 
¿Cómo haríamos para calcular un promedio de diez números dentro de un array? Simple, sumamos los números y dividimos el resultado por 10. Hagámoslo en Python:

Array_aleatorio = np.random.randint(10,size=10)
print(Array_aleatorio)
suma = 0
for i in Array_aleatorio:
    suma += i
promedio = suma / np.size(Array_aleatorio)
print(promedio)

Esta resolución es bonita y elegante. No obstante, es posible que debamos calcular frecuentemente este tipo de medidas resumen, como el promedio, la varianza, el desvío, la mediana, y similares. Para estos casos frecuentes, NumPy tiene atajos que son muy útiles a la hora de realizar los cálculos.

print(Array_aleatorio.sum()) # Suma de elementos
print(Array_aleatorio.mean()) # Promedio de elementos
print(Array_aleatorio.max()) # Elemento más grande.
print(np.median(Array_aleatorio)) # Mediana
print(np.std(Array_aleatorio)) # Desvío estándar
print(np.var(Array_aleatorio)) # Varianza

Todas las funciones pueden escribirse como np.nombre_de_función(objeto). Las funciones más comunes (sum, mean, max), pueden escribirse equivalentemente como métodos aplicados sobre el objeto (por ejemplo objeto.mean().
De esta manera NumPy organiza las funciones de agregación, o resumen, de forma compacta y en una sola línea de código.
Es necesario aclarar que Python ofrece estas funciones por defecto, pero en NumPy están optimizadas para trabajar con grandes volúmenes de datos.
## Operaciones vectorizadas
Finalmente, NumPy trae un conjunto de funciones para operaciones optimizadas para arrays, de tal forma de trabajar estas estructuras a la manera de vectores o matrices matemáticas. A estas funciones se las llama operaciones vectorizadas, o funciones universales (ufuncs). Muchas veces es necesario aplicar operaciones sobre cada elemento, como por ejemplo sumar una constante, o bien sumar dos vectores elemento a elemento, o realizar un producto matricial. Para ello podemos operar utilizando estas funciones con los ndarrays de NumPy. Veamos algunos ejemplos:

print(Array_1, Array_2) 
print(Array_1 + 5) # Suma 5 a cada elemento de Array_1
print(Array_1 + Array_2) # Suma Array_1 y Array_2, elemento a elemento
print(np.add(Array_1,Array_2)) # Igual al anterior
print(np.matmul(Array_1, Array_2)) # Producto vectorial: Se multiplican los elementos en la misma posición de Array_1 y Array_2 (se multiplican los dos primeros, luego los dos segundos, etc.), y luego se suman todos los resultados.

La guía completa de referencia de las ufuncs está disponible en https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs  
Siempre que se trabaje con ndarrays de NumPy se recomienda utilizar estas funciones, porque además de ser más compactas que realizar la programación a mano, están construidas de tal forma que funcionan más rápidamente. Esto es especialmente importante cuando utilizamos conjuntos grandes de datos.



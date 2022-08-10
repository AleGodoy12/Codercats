#  Diccionarios 🐍

1. ¿Que son? - ¿Para que sirve?
2. Sintaxis
3. Ejemplo

![Diccionarios](/imagenes/diccionarios.png)

### ¿Qué son y para que sirve?

#### Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave (Key).

1. Para definir un diccionario, se encierra el listado de valores entre llaves. Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos.
![Diccionarios](/imagenes/diccionarios1.png)

2. Podemos acceder al elemento de un Diccionario mediante la clave de este elemento, como veremos a continuación:

![Diccionarios](/imagenes/diccionarios2.png)

3. También es posible insertar una lista dentro de un diccionario. Para acceder a cada uno de los cursos usamos los índices:

![Diccionarios](/imagenes/diccionarios3.png)

4. Para recorrer todo el Diccionario, podemos hacer uso de la estructura for:

![Diccionarios](/imagenes/diccionario4.png)

# Operaciones

### Los objetos de tipo diccionario permite una serie de operaciones usando operadores integrados en el interprete Python para su tratamiento, a continuación algunos de estos:

1. Acceder a valor de clave: 
#### Esta operación le permite acceder a un valor especifico del diccionario mediante su clave.

![Diccionarios](/imagenes/diccionarios5.png)

2. Asignar valor a clave
#### Esta operación le permite asignar el valor especifico del diccionario mediante su clave.

![Diccionarios](/imagenes/diccionarios6.png)

3. Iteración in:
#### Este operador es el mismo operador integrado in en el interprete Python pero aplicada al uso de la secuencia de tipo diccionario

![Diccionarios](/imagenes/diccionarios7.png)

# Metodos
## Los objetos de tipo diccionario integra una serie de métodos integrados a continuación:

1. dict (): Recibe como parámetro una representación de un diccionario y si es factible, devuelve un diccionario de datos.

![metodos](/imagenes/metodos.png)

2. zip(): Recibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla. Ambos parámetros deben tener el mismo número de elementos. Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables.

![metodos](/imagenes/metodos1.png)

3. items(): Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.

![metodos](/imagenes/metodos2.png)

4. keys(): Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario

![metodos](/imagenes/metodos3.png)

5. values(): Retorna una lista de elementos, que serán los valores de nuestro diccionario.

![metodos](/imagenes/metodos4.png)

6. clear(): Elimina todos los ítems del diccionario dejándolo vacío.
![metodos](/imagenes/metodos5.png)

7. copy(): Retorna una copia del diccionario original.
![metodos](/imagenes/metodos6.png)

8. fromkeys(): Recibe como parámetros un iterable y un valor, devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. Si el valor no es ingresado, devolverá none para todas las claves.
![metodos](/imagenes/metodos7.png)

9. get(): Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none

![metodos](/imagenes/metodos8.png)

10. pop(): Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.

![metodos](/imagenes/metodos9.png)

11. setdefault(): Funciona de dos formas. En la primera como get.
![metodos](/imagenes/metodos10.png)

#### Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.

![metodos](/imagenes/metodos11.png)

12. update(): Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor es agregado al diccionario.
![metodos](/imagenes/metodos12.png)


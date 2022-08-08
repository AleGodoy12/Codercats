#  Funciones 🐍

1. ¿Que son? - ¿Para que sirve?
2. Sintaxis
3. Ejemplo

![funciones](/imagenes/funciones.png)

### ¿Que son y para que sirven las funciones?

### Una función es una porción o bloque de código reutilizable que se encarga de realizar una determinada tarea.
### Cualquier función tendrá un nombre, unos argumentos de entrada, un código a ejecutar y unos parámetros de salida.
### Las funciones nos ayudan a generar un codigo mas limpio y escalable porque cumplen con dos principios claves: 
### 1. El principio de reusabilidad, que nos dice que si por ejemplo tenemos un fragmento de código usado en muchos sitios, la mejor solución sería pasarlo a una función. Esto nos evitaría tener código repetido, y que modificarlo fuera más fácil, ya que bastaría con cambiar la función una vez.
### 2. Principio de modularidad, que defiende que en vez de escribir largos trozos de código, es mejor crear módulos o funciones que agrupen ciertos fragmentos de código en funcionalidades específicas, haciendo que el código resultante sea más fácil de leer.


# Sintaxis

### Para declarar una función solo se debe poner la palabra "def" seguido del nombre de la función, para el ejemplo le hemos puesto "sumar", en los paréntesis deben ir los parámetros, ya hablaremos de eso más adelante, por último la palabra "pass" es el contenido de la función. Siempre tengan en cuenta la identación dentro de la función.
![ejemplo](/imagenes/funciones1.png)

## Para terminar con la función antes declara vamos a agregar el contenido.
![ejemplo](/imagenes/funciones2.png)

#### Con esto tenemos una función que suma 5 + 10, para llamar o activar a esta función, ponemos el nombre la función seguido de paréntesis.

## Parámetros

### Si bien en el ejemplo anterior creamos una función que suma 5 + 10 eso no es suficiente, ahora vamos a enviarle parámetros a esa función y sumar los datos que le enviemos.
![ejemplo](/imagenes/funciones3.png)

#### Con esto nuestra función sumar ahora recibe 2 parámetros, si ejecutan esto el resultado debe ser 25. Veamos otras variaciones de parametros.

![ejemplo](/imagenes/funciones4.png)
#### En este caso el parámetro number2 tiene un valor por defecto, esto quiere decir que cuando NO se le envie ese parámetro a la función, por defecto number2 tomará el valor de 20.

# Orden de los parámetros

### Cuando enviamos parámetros a una función, damos por hecho que el primer valor siempre va al primer parámetro, el segundo valor con el segundo parámetro, y así con todo los que haya, pero esto es algo que podemos cambiar gracias a Python.
![ejemplo](/imagenes/funciones5.png)

#### Al momento de llamar a la función, explícitamente le estamos diciendo que parámetro va a tomar que valor, para verificar esto, impriman number1 y number2 y verán el valor que tienen. Ya saben que no es necesario seguir el orden de los parámetros en la función, pueden enviar los parámetros en el orden que deseen pero siempre poniendo explícitamente el nombre del parámetro.


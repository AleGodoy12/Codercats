# # Ejercicios practicos Evaluacion 16-8

# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.
def par_impar(a):
    if a%2==0:
        cartel1="Es par"
        return cartel1
    else:
        cartel2="Es impar"
        return cartel2

num=int(input("Ingrese un numero: "))    #muestra
print(par_impar(num))

# 2. Crea una función que dados dos números mostrará todos los números que hay entre ellos
def showNumbers(a,b):
    lista=[]
    ma=max(a,b)
    mi=min(a,b)
    for i in range(mi+1,ma):
        lista.append(i)
    return lista

x=int(input("Ingrese un numero: "))        #muestra
y=int(input("Ingrese otro numero: "))
print(showNumbers(x,y))

# 3. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def validar(document):
    if len(document)==7 or len(document)==8:
        cartel="Documento valido"
        return cartel
    else:
        cartel1="Documento invalido"
        return cartel1

dni=input("Ingrese su numero de documento (sin puntos): ")
print(validar(dni))

# 4. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro
def ultima(array):
    lista=array.split()
    n=len(lista[-1])
    return n

string=input("Escriba una oracion: ")
print(ultima(string))

# 5. Realiza una función que sume dos números pasados por parámetros
def sumar(a,b):
    suma=a+b
    return suma

x=int(input("Ingrese un numero: "))        #muestra
y=int(input("Ingrese otro numero: "))
print(sumar(x,y))

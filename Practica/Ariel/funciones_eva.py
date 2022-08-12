# # Ejercicios practicos Evaluacion 16-8

# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.
num = int(input("Ingrese un número: "))

def validar(n):
    if n % 2 == 0:
        mensaje = f"El numero {n} es par"
    else:
        mensaje = f"El numero {n} es impar"
    return mensaje

num1 = validar(num)
print(num1)


# 2. Crea una función que dados dos números mostrará todos los números que hay entre ellos
inicio = int(input("ingrese un numero: "))
fin = int(input("ingrese otro numero: "))

def entreNum(comienzo, final):
    rango = []
    for i in range(comienzo, final):
        rango.append(i) 
    return rango

a = entreNum(inicio, fin)
print(a)



# 3. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
dni = input("Ingrese su numero de dni: ")

def verificarDni(dni):
    if len(dni) > 6 and len(dni) < 9:
        mensaje = f"El dni: {dni} es valido"
    else: 
        mensaje = f"El dni: {dni} es invalido"
    return mensaje

dni1 = verificarDni(dni)
print(dni1)


# 4. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro
oracion = input("Ingrese un string: ")
def ultPalabra(o):
    desarmada = o.split()
    ultima = desarmada[-1]
    return f"La ultima palabra, {ultima}, tiene una logitud de {len(ultima)} caracteres"

ora1 = ultPalabra(oracion)
print(ora1)



# 5. Realiza una función que sume dos números pasados por parámetros
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

def suma(num1, num2):
    return f"La suma es: {num1} + {num2} = {num1 + num2}"

suma1 = suma(n1, n2)
print(suma1)
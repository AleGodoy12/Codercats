# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.

def esPar(numero):
    if(numero % 2 == 0):
        return f'{numero} es par'
    return f'{numero} es impar'

numeroUsr = int(input("Ingresa un número: "))
print(esPar(numeroUsr))
    
# 2. Crea una función que dados dos números mostrará todos los números que hay entre ellos

def mostrarNumerosEnRango(num1, num2):
    desde = min(num1, num2)
    hasta = max(num1, num2)
    for i in range(desde+1, hasta):
        print(i)
      
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
mostrarNumerosEnRango(numero1, numero2)

# 3. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validarDni(dni):
    if(len(dni) > 6 and len(dni) < 9):
        return True
    return False

dniUsr = input("Ingresa tu DNI: ")
if(validarDni(dniUsr)):
    print("DNI válido")
else:
    print("DNI inválido")

# 4. Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro

def mostrarLongitud(texto):
    texto = texto.strip() #Saco los espacios al principio o al final del string
    listaPalabras = texto.split(" ")
    lenUltimaPalabra = len(listaPalabras[-1])
    return lenUltimaPalabra

textoUsr = input("Ingresa un texto: ")
print(mostrarLongitud(textoUsr))

# 5. Realiza una función que sume dos números pasados por parámetros

def sumar(num1, num2):
    return num1 + num2

print(sumar(24, 4))
print(sumar(24.3, 4.8))
# # Ejercicios practicos Evaluacion 16-8

# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.

# numeroPasado = int(input("Ingrese un numero: "))

# def esPar(numeroPasado):
#     if (numeroPasado%2 ==0):
#         return "El numero ingresado es un numero par"
#     else:
#         print("El numero ingresado es impar")        
# print(esPar(numeroPasado))

# 2. Crea una función que dados dos números mostrará todos los números que hay entre ellos
num1= int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
def numerosMedios(num1, num2):
    for i in range(num1+1, num2):
        print("Los numeros que se encuentran entre", num1,"y", num2, "son: ",i)
print(numerosMedios(num1, num2))

# 3. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
# dni = input("Ingrese su DNI:")
# longitud = len(dni)
# print(longitud)
# def dniValido(dni):
#     if (longitud== 7 or longitud==8):
#         return True
#     else:
#         return False
# print(dniValido(dni))

# 4. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro
frase= input("Ingrese una frase: ")
def longitud(frase):
   if (len(frase)== 0):
       return 0
   cant=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cant+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cant=0
   return cant
print(longitud(frase))

# 5. Realiza una función que sume dos números pasados por parámetros
numA = int(input("Ingrese un número: "))
numB = int(input("Ingrese otro número: "))

def sumando(numA, numB):
    return numA + numB

print("La suma de los numeros ingresados es =",sumando(numA, numB))
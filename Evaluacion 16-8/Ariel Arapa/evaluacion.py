# # Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos
print("Ingrese dos numeros y le mostramos los numeros internos!")
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

def numInternos(n1, n2):
    z = []
    if n1 < n2:
        for x in range(n1, n2):
            z.append(x)
    else: 
        for x in range(n2, n1):
            z.append(x)
    return z

internos1 = numInternos(num1, num2)
print(internos1)


# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
x = input("Ingrese un dni: ")

def validarDni(dni):
    if len(dni) >= 7 and len(dni) < 9:
        mensaje = f"El d.n.i. ingresado {dni} es valido"
    else:
        mensaje = f"El d.n.i. ingresado {dni} es invalido"
    return mensaje 

validar1 = validarDni(x)
print(validar1)


# 3. Crea una funcion que retorne tu nombre y color favorito.
name = input("Ingrese su nombre: ")
color = input("Ingrse su color favorito: ")

def mensaje(name, color):
    return f"{name} tu color favorito es {color}"

mensaje1 = mensaje(name, color)
print(mensaje1)
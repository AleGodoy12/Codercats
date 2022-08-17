# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

def mostrarNumerosEnRango(num1, num2):
    desde = min(num1, num2)
    hasta = max(num1, num2)
    for i in range(desde+1, hasta):
        print(i)
      
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
mostrarNumerosEnRango(numero1, numero2)

# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validarDni(dni):
    if(type(dni) == str and dni.isdigit() and len(dni) > 6 and len(dni) < 9):
        return True
    return False

dniUsr = input("Ingresa tu DNI: ")
if(validarDni(dniUsr)):
    print("DNI válido")
else:
    print("DNI inválido")

# 3. Crea una funcion que retorne tu nombre y color favorito.

def mostrarGusto(nombre, color):
    return f'{nombre} tu color favorito es {color}'

nombre = 'Jorge'
colorFav = 'Negro'

print(mostrarGusto(nombre, colorFav))

#Jorge, bien planteadas las resoluciones, usando ademas conocimientos adquiridos de forma autodidacta.
#10/10
# # Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

def numeros (num1, num2):

    while num1 < num2:
        num1 += 1
        print(num1)

numeros (5, 10)


# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI 
# sea válido debe tener entre 7 y 8 dígitos.

def comprobacionDNI(dni):
    if len(dni) == 7 or len(dni) == 8:
        return True
    else:
        return False

print(comprobacionDNI(str(38991263)))


# 3. Crea una funcion que retorne tu nombre y color favorito.


def favoritos(nombre, color):

    return (f"Tu nombre es {nombre} y tu color favorito es {color}")


print(favoritos("Airton","violeta" ))
    
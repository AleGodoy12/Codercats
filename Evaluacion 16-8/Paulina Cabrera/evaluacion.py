# Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

# num1 = int(input("Ingrese un número: "))
# num2= int(input("Ingrese otro número: "))

# def entreEllos(num1, num2):
#     for i in range(num1 +1, num2):
#         print(f"Los numeros que se encuentran entre {num1} y {num2}: {i}")
# print(entreEllos(num1, num2))


# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

dni = (input("Ingrese su número de DNI: "))

def dniValido(dni):
    if (len(dni)==7 or len(dni)==8):
        return (f"El DNI: '{dni}' es válido")
    else:
        return (f"El DNI: '{dni}' es inválido")
print(dniValido(dni))
# 3. Crea una funcion que retorne tu nombre y color favorito.

# nombre= input("Ingresa tu nombre: ")
# color= input("Ingresa tu color favorito: ")

# def nombreycolor(nombre, color):
#     return (f"¡Hola! tu nombre es: {nombre} y tu color favorito es: {color}")
# print(nombreycolor(nombre, color))

#Paulina, muy pero muy bien la resolucion y el planteo de los practicos. Vas cada dia mejorando la logica y 
#las formas en las que escribes el codigo, se nota mucho el interes y el compromiso.

#10/10
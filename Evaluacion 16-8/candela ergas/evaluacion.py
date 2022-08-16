# Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

def todos(numA,numB):
    for i in range(numA,numB):
        print(i)   
todos(1,10)

# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def dni(nro):
    nro=str(nro)
    return len(nro)==7 or len(nro)==8    
print(dni(123492222))

# 3. Crea una funcion que retorne tu nombre y color favorito.
nombre=input("Ingresá tu nombre: ")
color=(input("Ingresá tu color favorito: "))

def datos(nombre,color):
    return(nombre + " tu color favorito es: "+ color)
print(datos(nombre,color))




# Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos
def numInternos(a,b):
    maximo=max(a,b)
    minimo=min(a,b)
    numeros=[]
    for i in range(minimo+1,maximo):
        numeros.append(i)
    return numeros
    

num1=int(input("Ingrese un numero: "))            
num2=int(input("Ingrese otro numero: "))
print("Los numeros que hay entre ellos son: ", numInternos(num1,num2))   #verificacion

# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def validar(a):
    if len(a)==7 or len(a)==8:
        cartel="Documento valido"
        return cartel
    else:
        cartel="Documento invalido"
        return cartel

doc=input("Ingrese su numero de dni: ")
print(validar(doc))      #verificacion


# 3. Crea una funcion que retorne tu nombre y color favorito.
def datos(x,y):
    datos={}
    datos.update({"nombre":x,"color favorito":y})
    return datos

nombre=input("Ingrese su nombre: ")
color=input("Ingrese su color favorito: ")
print(datos(nombre,color))          #verificacion


#Abril, muy bien el planteo de los ejercicios y mucho mejor aun el uso de metodos para simplificarlo
#10/10
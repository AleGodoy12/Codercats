# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

direccion=input("Ingresá tu mail por favor: ")
if ("@" in direccion):
    print("Dirección valida")
else:
    print("Direccion invalida!")
    
# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

def sumando(n):
    digitos=[int(x) for x in str(n)]
    a=0
    for i in digitos:
        a+=i
    return a

nUser=input("Ingrese numeros: ")

def muestra(nUser):
    while nUser!="0":
        print("La suma de los digitos ingresados es: ",sumando(nUser))
        nUser=input("Ingrese numeros: ")
    (print("Bucle finalizado"))
muestra(nUser)

# Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, 
# mostrar la sumatoria de todos los números ingresados 
# y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.

def sumaAr(lista):
    c=0
    for n in lista:
        if type(n)!=int:
            c+= eval(n)
        else: 
            c+=n
    return c

nUser=input("Ingrese numeros: ")
def e2(nUser):
    numeros=[]
    digitos=[]
    while nUser!="0":
        numeros.append(nUser)
        digitos.append(sumando(nUser))
        print("La suma de los digitos ingresados es: ",sumando(nUser))
        nUser=input("Ingrese numeros: ")
    print("Bucle finalizado")
    print("La suma total de los numeros ingresados es: ",(sumaAr(numeros)))
    print("La suma total de los dígitos ingresados es: ",(sumaAr(digitos)))
e2(nUser)

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

# direccion=input("Ingresá tu mail por favor: ")

# if ("@" in direccion):
#     print("Dirección valida")
# else:
#     print("Direccion invalida!")
# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos 
# (utilizando una función que realice dicha suma)

# def sumaD(a): 
#     digitos=[int(x) for x in str(a)]
#     a=0
#     for i in digitos:
#         a+=i
#     return a
nUser=input("Ingrese numeros: ")
def muestra(nUser):
    while nUser!="0":
        digitos=[int(x) for x in str(nUser)]
        a=0
        for i in digitos:
            a+=i
        print("La suma de los digitos ingresados es: ", a)
        nUser=input("Ingrese numeros: ")
    (print("Bucle finalizado"))
muestra(nUser)

# Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, 
# mostrar la sumatoria de todos los números ingresados 
# y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.
nUser=input("Ingrese numeros: ")
def muestra(nUser):
    while nUser!="0":
        digitos=[int(x) for x in str(nUser)]
        a=0
        numeros=[]
        for i in digitos:
            a+=i
            numeros.append(a)
        print("La suma de los digitos ingresados es: ", a)
        nUser=input("Ingrese numeros: ")
    print(numeros)
    (print("Bucle finalizado"))
muestra(nUser)


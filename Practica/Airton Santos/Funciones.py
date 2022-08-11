# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose 
# de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

def direccionMail ():
    email = input("Ingrese una dirección de mail")

    i = ""

    for i in email:

        if email.find("@") >= 0:
            print("Es válida")
        else:
            print("No es una dirección válida, vuelva a intentarlo")
            email = input("Ingrese una dirección de mail")

direccionMail()



# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la 
# suma de sus dígitos (utilizando una función que realice dicha suma)


def sumaTotal():

    numero = input("Ingrese un número")
    suma = 0

    while numero != "0":
        for i in numero:
            suma += int(i)
        print(suma)
        suma = 0 
        numero = input("Ingrese un número")      
sumaTotal()

#3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en 
# el ejercicio 2.

def sumaTotal2():

    numero = input("Ingrese un número")
    suma = 0
    acumulador = 0 
    x = 0

    while numero != "0":  

        acumulador += int(numero)
        print(f"La sumatoria de los números ingresados es {acumulador}")

        for i in numero:
            suma += int(i)  
        print(f"La sumatoria de los dígitos ingresados es {suma}")

        numero = input("Ingrese un número")      

sumaTotal2()
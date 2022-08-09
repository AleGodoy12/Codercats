# Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"
# correo= input("Ingrese su correo electronico: ")

# def email(correo):
#     return correo
# if("@" in correo):
#     print("El email ingresado es válido")
# else:
#     print("El email ingresado es invalido, intente con un email válido")
    
# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

num= int(input("Ingrese un número: "))
def numeritos(num):
    suma=0
    while (num!=0):
        sumdigitos=  num%10
        suma= suma+sumdigitos
        num= num//10
    return suma

while (num!=0):
    print("La suma de las cifras es:",numeritos(num))
    num= int(input("Ingrese un número: "))
print("Ingresaste cero y el cero cierra el bucle :)")


# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.


# no funciona 

# suma = 0

# while (num!=0):
#     print("Suma:",numeritos(num))
#     suma= suma+num
#     num= int(input("Ingrese un número: "))
#     print("Suma total:", suma)
#     print("Suma dígitos:", numeritos(suma))
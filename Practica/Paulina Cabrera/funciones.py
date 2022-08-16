# Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"
# correo= input("Ingrese su correo electronico: ")

def email(correo):
    return correo
if("@" in correo):
    print("El email ingresado es válido")
else:
    print("El email ingresado es invalido, intente con un email válido")
    
# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

def  sumadigitos (a) : # defino funcion (a) puede val
    digitos =[int (x) for x in str(a)]   #va a leer el elemento
    acumulador = 0   #declaro el acumulador ene su posicion
    for i in digitos:
        acumulador+=i
    return acumulador
numero = input("ingrese un numero: ")
while numero !="0": # cero como string
    print (sumadigitos(numero))
    numero = input("ingrese un numero [para detener el programa ingrese 0]: ")
print ("bucle finalizado")

# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.


sumatoria=0
while numero!=0:
    print("La suma de los digitos:",sumadigitos(numero))
    sumatoria= sumatoria+int(numero)
    numero=int(input("Ingrese un número: [para detener el programa ingrese 0] "))
print("La suma total es:", sumatoria)
print("La suma de los digitos:", sumadigitos(sumatoria))
# #tarea funciones

# # Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"
def validar(correo):
    acumulador=0
    for i in correo:
        if i=="@":
            acumulador+=1
    if acumulador==1:
        cartel1="Correo valido"
        return cartel1
    else:
        cartel2="Correo invalido"
        return cartel2

mail=input("Ingrese su correo electronico: ")
print(validar(mail))

# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)
def sumaDigitos(a):
    digits=[int(x) for x in str(a)]
    acumulador=0
    for i in digits:
        acumulador+=i
    return acumulador
    
num=input("Ingrese un numero: ")

while num!="0":
    print("La suma de los digitos es: ", sumaDigitos(num))
    num=input("Ingrese un numero: ")
print("Bucle finalizado")


# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.

lista=[]   
num=input("Ingrese un numero: ")
while num!="0":
    lista.append(num)   
    print("La suma de los digitos es: ", sumaDigitos(num))
    num=input("Ingrese un numero: ")
    
acum=0                          
for n in lista:
    acum+=eval(n)       #eval pasa str a int                  
print("La suma de los numeros ingresados es: ", acum) 

acum2=0
for n in lista:
    acum2+=sumaDigitos(n)
print("La suma de los digitos de los numeros ingresados es: ", acum2)
# # Tuplas

# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero
meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
num=int(input("Ingrese un numero: "))

while num!=0:
    if num>=1 and num<=len(meses):
        print(meses[num])
        num=int(input("Ingrese un numero: "))
    else:
        print("Error")
        break

# 2.  Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
numeros=(1,13,11,2,2,2,1,3,4,6,5,7,8,9,20,10,4,5)
num=int(input("Ingrese un numero: "))
n=numeros.count(num)
print("El numero ", num , " aparece ", n ," veces.")

# 3. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla
numeros=(1,2,3,4,5,6,7,8,9,10)
num=int(input("Ingrese un numero: "))
print(numeros[num])

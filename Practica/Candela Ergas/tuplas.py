# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero

meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
num=int(input("Ingresá un nro entre el 1 y el 11: "))
while num: 
    if num>=1 and num<=(len(meses)-1):
        print(meses[num])
        num=int(input("Ingresá otro nro entre el 1 y el 11: "))
    elif num==0:
        break
    else:
        print("error!")
        num=int(input("Ingresá un nro entre el 1 y el 11: "))

#2.  Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

nros=(1,2,3,1,2,3,3,4,50,50)
print(nros)
num=int(input("Igresa un numero para ver cuantas veces se repite :) "))
print ("El numero",num,"se repite ",nros.count(num)," veces")

#3. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla

nros=(1,2,3,4,5,6,7,8,9,10)
nro=int(input("Ingresa el nro de indice: "))
print("El valor de ese indice es: ", nros[nro])


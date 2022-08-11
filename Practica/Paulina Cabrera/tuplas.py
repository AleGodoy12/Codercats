# # Tuplas

# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
meses =("enero","febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

cant= len(meses)
ingrese = int(input("Ingrese un numero del 1 al 12: "))

while (ingrese != 0):
    if (ingrese>=1 and ingrese< cant):
        print(meses[ingrese-1])
        ingrese = int(input("Ingrese un numero del 1 al 12: "))     
    else:
        print("Solo ingrese numeros del 1 al 12")
        break

# El programa termina cuando el usuario introduce un cero

# 2.  Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
tuplita = (1,1,1,1,2,2,3,4)
numero = int(input("ingrese un numero: "))

if tuplita[numero]:
    print("El numero ingresado se repite: ", tuplita.count(numero), "veces")
else:
    print("El numero ingresado no se encuentra en la tupla")


# 3. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla

valores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

buscado = int(input("Ingrese el numero que esta buscando: "))

if buscado>=0 and buscado<len(valores):
    print("El numero", buscado, "se encuentra en la posicion ",valores[buscado])
else:
    print("la tupla contiene 10 elementos :(")
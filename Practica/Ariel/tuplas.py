# # Tuplas

# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero

meses = ("Enero",  "Febrero","Marzo",  "Abril", "Mayo","Junio","Julio",  "Agosto","Septiembre", "Octubbre", "Noviembre","Diciembre")
while True:
    try:
        n = int(input("Ingrese un numero: "))
        if n >= 1 and n <= len(meses):
            print("Contenido en la posicion: ", meses[n])
        elif n == 0:
            break
        else:
            print("Numero fuera de rango")
    except IndexError:
        print("Numero fuera de rango")



# 2.  Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
num = (1, 2, 3, 2, 3, 1, 1, 2, 5, 6, 4)
n = int(input("Ingrese un numero: "))
cantidad = num.count(n)
print(f"Hay {cantidad} del numero {n} en la tupla")


# 3. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla
tu = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
indice = int(input("Ingrese un indice: "))
a = tu[indice]
print("El indice es " + str(indice) + " y su valor es " + str(a))
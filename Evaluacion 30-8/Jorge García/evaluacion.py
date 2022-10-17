# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

materias = {
    "Matemática": "Pablo",
    "Lengua": "Maria",
    "Inglés": "Pepe",
    "Cívica": "Daniela",
    "Física": "Juan",
    "Geografía": "Andrea"
}

print(materias)
materias["Matemática"] = "Jorge"
materias["Física"] = "Lucia"
print(materias)

# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor

listaNumeros = []
while True:
    numero = int(input('Número [0 para salir]: '))
    if(numero == 0):
        break
    listaNumeros.append(numero)
listaNumeros.sort(reverse=True)
print(listaNumeros)

# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
while True:
    numero = int(input("Ingresa un número [0 para salir]: "))
    if numero == 0: 
        break
    if(numero >= 1 and numero <= len(meses)): 
        print(f'Mes: {meses[numero-1]}')
    else: 
        print("¡Error! El número esta fuera de rango [entre 1 y 12]")
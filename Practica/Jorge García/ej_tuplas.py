# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta 
# entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.

meses = ("Enero", "Febrero", "Marzo", 
        "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", 
        "Octubre", "Noviembre", "Diciembre")
numero = None
while numero != 0:
    numero = int(input("Ingresa un número [0 para salir]: "))
    if numero == 0: 
        continue
    if(numero >= 1 and numero <= len(meses)):
        print(f'Mes: {meses[numero-1]}')
    else: 
        print("¡Error! El número esta fuera de rango [entre 1 y 12]")
        
# # 2. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

numeros = 1, 2, 2, 2, 10, 6, 8, 8, 9, 10, 8, 2
print(f'Tupla: {numeros}')
numero = int(input("Ingresa un número: "))
contador = numeros.count(numero)
print(f'Repeticiones de {numero}: {contador} {"vez" if contador == 1 else "veces"}')

# 3. Crea una tupla con valores ya predefinidos del 1 al 10, 
# pide un índice por teclado y muestra los valores de la tupla

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(numeros)
indice = int(input("Indice: "))
if(indice >= 0 and indice <= len(numeros)-1):
    print(f"Valor = {numeros[indice]}")
else:
    print(f"¡Fuera de rango! El último indice es: {len(numeros)-1}")
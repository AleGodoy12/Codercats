# # Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes


# mes = {1:"enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre" }

# fecha = input("Introduzca una fecha con el siguiente formato: [dd/mm/aaaa] ")
# fecha = fecha.split("/") #permite usar / en el imput

# print(fecha[0], 'de', mes[int(fecha[1])], 'del', fecha[2])


# 2. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# diccionario = {}

# programa = str(input("Introduzca una lista de palabras en español y luego en ingles, siguiendo el siguiente formato [palabra:traducción] separadas por comas:"))

# for i in programa.split(","):
#     clave, valor = i.split(":")
#     diccionario[clave]= valor

# traduccion = input("Escriba la frase que quiere traducir: ")

# for t in traduccion.split(" "):
#     if t in diccionario:
#         print(diccionario[t], end=" ")
#     else:
#         print( t, end= " ")

# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

datos = {"nombre": "Paulina",
"Edad":19, 
"Estudia": "Programacion",
"Mascotas": ["perro", "gato","hamster" ],
"comida": "ñoquis"}

# #pop
borrado = datos.pop("comida")
print("El elemento", borrado ,"fue borrado con el metodo POP y el diccionario quedo asi",datos)

# #update
datos.update({"Trabaja": True})

print("Se agrego un nuevo elemento con el metodo UPDATE y quedo asi: ",datos)

#get

valor = datos.get("nombre")
print("Obtuve el valor de la clave con el metodo GET: ",valor)

# #copy

copiado = datos.copy()
print("Esta es la copia: ",copiado)

#zip
atr1= ["hijos"]
atr2=[False]
dic= dict(zip( atr1, atr2))
datos.update(dic)
print(dic)




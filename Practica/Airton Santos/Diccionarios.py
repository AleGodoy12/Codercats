# Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> 
# de aaaa donde <mes> es el nombre del mes.

meses = {"01" :"Enero", 
        "02" :"Febrero",
        "03" : "Marzo",
        "04" : "Abril", 
        "05" : "Mayo", 
        "06" : "Junio",
        "07" : "Julio",
        "08" : "Agosto",
        "09" : "Septiembre",
        "10" : "Octubre",
        "11" : "Noviembre",
        "12" : "Diciembre",
        
}

def preguntarFecha():

    fecha = input("Ingrese una fecha en formato dd/mm/aaaa")
    mes = fecha[3] + fecha[4]
    mesMostrado = meses.get(mes)

    print(fecha[:2], "de", mesMostrado, fecha[-4:])

preguntarFecha()

# 2. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e 
# inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras 
# y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

dicTraduccion = {}
listaTraduccion = []

def traductor():

    i = 0
    while i < 6:
        palabras = input("Ingrese una palabra en formato ESPAÑOL:INGLES")

        npalabras = palabras.split(":")
        palabraEsp = npalabras[0]
        palabraEng = npalabras[1]


        dicTraduccion.update({palabraEsp:palabraEng})

        i += 1
        print(dicTraduccion)

traductor()

listaVacia = []
frase = input("Ingrese una frase en español para traducir")
fraseSeparada = frase.split(" ")
# listaVacia.append(fraseSeparada)
claves = dicTraduccion.keys()

fraseTraducida = ""

for i in fraseSeparada:
    if dicTraduccion.get(i)!= None:
        fraseTraducida += dicTraduccion[i] + " "
    else:
        fraseTraducida += "No hay traduccion disponible"
print(fraseTraducida)

# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

dicA = {1: "Menta", 2: "Chocolate", 3: "Frutilla"}
dicB = {4: "Vainilla", 5: "Dulce de leche", 6: "Pistcho"}

#Saco el gusto menta del dicA
menta = dicA.pop(1)

#Agrego menta al dicB
dicB.update({7:menta})
print(dicB)

#Consulto el valor del key 2 del dicA
consulta = dicA.get(2)
print(consulta)

#Nuevo diccionario a partir del dicB

nuevoDic = dicB.copy()
print(nuevoDic)

#Junto ambos diccionarios

union = zip(dicA, dicB)

print(tuple(union))
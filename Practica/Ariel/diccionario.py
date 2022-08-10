# # Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes
meses = {"01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubbre", "11": "Noviembre", "12": "Diciembre"}
fecha = input("Ingrese la fecha dd/mm/aaaa: ")
listaFecha = fecha.split("/")
dia = listaFecha[0]
mes = listaFecha[1]
año = listaFecha[2]
for x in meses:
    if x == mes:
        print(f"{dia} de {meses[x]} de {año}!")


# 2. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
dicc = {}
while True:
    palabra = input("Ingrese una palabra en español e ingles: ")
    if palabra == "Salir" or palabra == "salir":
        break
    espa, ingles = palabra.split(",")
    if dicc.get(espa) == None:
        dicc.update({espa : ingles})
    else:
        print("Ya ingresaste esas palabras!")

fraseEspa = input("Introduzca una frase en español: ")
fraseIngles = ""
listaFrase = fraseEspa.split()

#print(listaFrase)

for x in listaFrase:
    if dicc.get(x) != None:
        fraseIngles += dicc[x] + " "
    else: 
        fraseIngles += " *** "
print(fraseIngles)

# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.
auto = {"marca": "BMW", "patente": "AH1-2AS", "puertas": 2}
print("Diccionario incial: ", auto)

auto.pop("puertas")
print("Diccionario usando el pop: ", auto)

auto.update({"polarizado": True})
print("Diccionario usando el update: ", auto)

validar = auto.get("puertas")
print("Diccionario usando el get: ", validar)

auto2 = auto.copy()
print("Diccionario usando el copy: ", auto2)

for a, b in zip(auto, auto2):
    print(f"Auto: {a} y auto2: {b}")
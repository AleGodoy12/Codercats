# # Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes
meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

dia=int(input("Ingrese el dia de la fecha :"))
mes=int(input("Ingrese el mes (numericamente): "))
año=int(input("Ingrese el año: "))

print(dia, " de ", meses[mes-1], " del ", año )

# 2. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
traductor={}
ing_esp=input("Escriba una palabra en español e ingles respectivamente separada por dos puntos ")
while ing_esp!="basta":
    español,ingles = ing_esp.split(":")
    traductor.update({español:ingles})
    ing_esp=input("Escriba una palabra en español e ingles respectivamente separada por dos puntos (escribir basta cuando desee terminar)")
print(traductor)  #demostracion de diccionario ingles-español

frase=input("Escriba una frase en español ")
arrayFrase=frase.split()
traduccion=[]
for i in arrayFrase:
    e=traductor.get(i)
    traduccion.append(e)

texto=" "
for palabra in traduccion:
    texto += palabra + " "
print(texto.strip())     #texto traducido


# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.
keys=["nombre","edad","tipo","sexo"]
value=["Po",3,"perro","masculino"]
dicc=dict(zip(keys,value))
s=dicc.pop("sexo")
dicc.update({"color":"gris"})
n=dicc.get("nombre")
dicc1=dicc.copy()

print(dicc1, n, s)   #demostracion 
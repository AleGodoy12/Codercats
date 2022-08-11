# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes

meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
    7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

fechaUsr = input("Fecha [dd/mm/aaaa]: ")
fechaSeparada = fechaUsr.split('/') #.-Guardo en una lista dia, mes y año separados.

if(len(fechaSeparada) == 3 and int(fechaSeparada[0]) > 0 and int(fechaSeparada[0]) <= 31):
    mes = int(fechaSeparada[1])
    if(meses.get(mes) != None): #.-Pregunto si el mes existe.
        print(f'Día {fechaSeparada[0]} de {meses[mes]} del {fechaSeparada[2]}') 
    else:
        print("¡Mes inválido!") 
else:
    print("Fecha inválida")

# 2. Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

traducciones = {}
palabrasUsr = input("Ingresa las traducciones [<español>:<inglés>]: ").lower()
# palabrasUsr = "hola:hello, adios:bye, correr:run, lentes:glasses, mesa:table, invierno:winter"
palabrasUsr = palabrasUsr.replace(" ", "")
palabrasUsr = palabrasUsr.split(",")
# print(palabrasUsr)
for i in palabrasUsr:
    traduccion = i.split(":")
    traducciones[traduccion[0].capitalize()] = traduccion[1].capitalize()
# print(traducciones)

palabraEsp = input("Ingresa una palabra en español: ").capitalize()
palabraEng = traducciones.get(palabraEsp)
if(palabraEng != None):
    print(f'Traduccion de {palabraEsp} --> {palabraEng}')
else:
    print("No tengo esa traducción, vuelve más tarde.")

# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

persona = {
    "nombre": "Pepe",
    "dni": 45873456,
    "edad": 28,
    "altura": 1.75,
    "sexo": "Hombre",
    "profesion": "Programador",
    "tienePerro": True
}

atributoEliminado = persona.pop("altura")
print(f'Se elimino el valor: {atributoEliminado}')
persona.update({"tieneGato": False})
persona.update({"apellido": "Diaz"})
persona.update({"profesion": "Tester"})
print(f'Después del update: {persona}')

prueba = persona.get("edad")
print(prueba)
prueba2 = persona.get("peso", "No esta el peso")
print(prueba2)

copiaPersona = persona.copy()
print(f"Copia de persona: {copiaPersona}")

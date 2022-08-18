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

# # 2. Escribir un programa que cree un diccionario de traducción español-inglés. 
# # El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# # y cada par <palabra>:<traducción> separados por comas. 
# # El programa debe crear un diccionario con las palabras y sus traducciones. 
# # Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# # Si una palabra no está en el diccionario debe dejarla sin traducir.

traducciones = {}
palabrasUsr = input("Ingresa las traducciones [<español>:<inglés>]: ").lower()
# palabrasUsr = "hola:hello, adios:bye, correr:run, lentes:glasses, mesa:table, invierno:winter"
palabrasUsr = palabrasUsr.replace(" ", "")
palabrasUsr = palabrasUsr.split(",")
for i in palabrasUsr:
    traduccion = i.split(":")
    traducciones[traduccion[0]] = traduccion[1]
    
texto = input("Ingresa un texto en español: ").lower()
# texto = 'hola como estas estamos en invierno adios'
texto = texto.split(" ")
traduccion = ""
for palabra in texto:
    palabraEng = traducciones.get(palabra)
    if(palabraEng != None):
        traduccion += palabraEng + " "
    else:
        traduccion += palabra + " "
print(traduccion)

# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

persona = {
    "nombre": "Pepe",
    "dni": 45873456,
    "edad": 28,
    "altura": 1.75,
    "profesion": "Programador",
    "tienePerro": True
}

atributoEliminado = persona.pop("altura")
print(f'\nSe elimino el valor: {atributoEliminado} del diccionario')
persona.update({"apellido": "Diaz"})
persona.update({"profesion": "Tester"})
print(f'\nDespués del update: {persona}')

print("\nSe obtuvo la edad con el get")
prueba = persona.get("edad")
print(prueba)
prueba2 = persona.get("peso", "No esta el peso")
print(prueba2)

print("\nSe copio la persona con el copy")
copiaPersona = persona.copy()
print(f"Copia de persona: {copiaPersona}")

dicConZip = dict(zip(["tieneGato", "email", "nacionalidad"], [False, "pepe@gmail.com", "portugués"]))
persona.update(dicConZip)
print("\nSe agrego el diccionario hecho con el zip a persona")
print(persona)
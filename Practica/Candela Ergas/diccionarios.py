# Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes
meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio",7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

fecha = input("Ingresá una fecha (dd/mm/aaaa) : ")
fechaS = fecha.split('/') 
mesD=int(fechaS[1])

print("La fecha ingresada es: ",fechaS[0]," de ",meses[mesD]," de ",fechaS[2])

# 2. Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas.
#  El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.
ejemplo={"num":30,"saludo":"hola","listA":(1,2,3),"numB":2.5}
print(ejemplo)

eliminado= ejemplo.pop("numB")
print(ejemplo,eliminado)

b={"saludo": "Hola!,como estas?"}
ejemplo.update(b)
print(ejemplo)

print(ejemplo.get("listA"))

ej2={"a":1,"b":2,"c":3,"d":4}
ejemplo=ej2.copy()
print(ejemplo)

nueva=dict(zip(["Argentina","Bolivia","Chile","Uruguay"],[100,200,300,400]))
print(nueva)

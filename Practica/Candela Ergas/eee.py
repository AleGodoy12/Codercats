traducciones = {}
palabrasUsr = input("Ingresa las traducciones [<español>:<inglés>]: ").lower()
# palabrasUsr = "hola:hello, adios:bye, correr:run, lentes:glasses, mesa:table, invierno:winter"
palabrasUsr = palabrasUsr.split(",")
print(palabrasUsr)
for i in palabrasUsr:
    traduccion = i.split(":")
    traducciones[traduccion[0].capitalize()] = traduccion[1].capitalize()
print(traducciones)
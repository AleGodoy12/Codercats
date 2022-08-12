dicc = {}
def diccionario ():
    palabraEspañol =  input('Ingresame una palabra en español')
    palabraIngles =  input('Ingresá su traducción')
    while (palabraEspañol == 'Listo'):
        dicc[palabraEspañol] = palabraIngles
        palabraEspañol =  input('Ingresame una palabra en español')
        palabraIngles =  input('Ingresá su traducción')
    return dicc

def traduccion ():
    frase =  input('Ingresá una frase')
    frase2 = frase.split( )
    i = 0
    while (i < len(frase2)):
        dicc.get(i)
        print (i)

diccionario()

#2 Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
# cada par :<traducción> separados por comas. El programa debe crear un diccionario con 
# las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario
#  para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin 
# traducir.
    


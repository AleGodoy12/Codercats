# #1
# print('Los siguientes datos deben ser ingresados de forma numérica dd/mm/aaaa')
# dia = input('Ingresá un día')
# mes = input('Ingresa un mes')
# año = input('Ingresá un año')
# meses = {'01': 'enero', '02':'febrero', '03':'marzo', '04':'abril','05':'mayo','06':'junio','07':'julio','08':'agosto','09':'septiembre','10':'octubre','11':'noviembre','12':'diciembre'}
# print ('La fecha que ingresaste es' , dia , 'de' , meses.get(mes) , 'de' , año)
    
# #2 Escribir un programa que cree un diccionario de traducción español-inglés. 
# # El usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
# # cada par :<traducción> separados por comas. El programa debe crear un diccionario con 
# # las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario
# #  para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin 
# # traducir.
# dicc = {}
# def diccionario ():
#     palabraEspañol =  input('Ingresame una palabra en español')
#     palabraIngles =  input('Ingresá su traducción')
#     while (palabraEspañol == 'Listo'):
#         dicc[palabraEspañol] = palabraIngles
#         palabraEspañol =  input('Ingresame una palabra en español')
#         palabraIngles =  input('Ingresá su traducción')
#     return dicc

# def traduccion ():
#     frase =  input('Ingresá una frase')
#     frase2 = frase.split( )
#     i = 0
#     while (i < len(frase2)):
#         dicc.get(i)
#         print (i)

# diccionario()

# #3
# dicc = {'nombre': 'Luján', 'edad': 24, 'color favorito': 'verde', 'mascota/s':'Brishito', 'lugar favorito': 'mi cama'}
# print('Diccionario original' ,dicc)

# dicc.pop('lugar favorito')
# print('Se borra lugar favorito' , dicc)

# print('acá vemos cual es mi color favorito:', dicc.get('color favorito'))

# copia = dicc.copy()
# print('acá hacemos una copia de dicc', copia)

# masMascotas = {'mascota/s': ['Brishito', 'Zico']}
# dicc.update(masMascotas)
# print('aca deberiamos ver como cambia de brishito a zico', dicc)

# clave = ['nombre', 'edad', 'color favorito']
# valor = ['lujan', 24, 'verde']
# dicc2 = dict(zip(clave, valor))

# for dato, info in zip(clave, valor):
#     print(dato,':', info,)


dicc = {}
#nombre es la clave y lujan es el valor
clave = input ('decime info que quieras agregar')
valor = input('info correspondiente')

dicc[clave] = valor
print(dicc)
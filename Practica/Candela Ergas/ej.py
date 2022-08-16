# Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, 
# mostrar la sumatoria de todos los números ingresados 
# y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.
# nUser=input("Ingrese numeros: ")
# def muestra(nUser):
#     while nUser!="0":
#         digitos=[int(x) for x in str(nUser)]
#         a=0
#         numeros=[]
#         numeros.append(nUser)
#         for i in digitos:
#             a+=i
#             print("La suma de los digitos ingresados es: ", a)
#             print("los num son", numeros)
#             nUser=input("Ingrese numeros: ")
            
#     (print("Bucle finalizado"))
# muestra(nUser)


# 2. Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas.
#  El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

dUser=input("Ingresá las palabras en español con su traduccion en inglés en el siguiente formato: español:inglés,español:inglés ")
print(dUser)
dUserr= dUser.split()
# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.


colegio={"frances":"Alexia", "ed fisica": "Jorge"}
def colegioMP():
    agregar= input("¿Desea agregar asignaturas? [S/N]")
    while agregar== "S":
        mat1= input("Ingrese el nombre de la materia que quiere agregar: ")
        prof1=input("Ingrese el nombre del profesor que dicta la materia que agrego: ")
        colegio.update({mat1:prof1})
        print(f"La materia {mat1} que la dicta el profesor {prof1} fue agregada con exito.")
        print(colegio)
        agregar= input("Desea agregar mas asignaturas? [S/N]")
    print("¡Asignaturas y docentes agregados!")
print(colegioMP())


#Editar docentes:
print(f"Actualmente asi esta la lista de docentes: {colegio}")
cambio=input("Indique la asignatura a la que quiere editar el docente: ")
nuevoValor= input("Indique el nuevo nombre del docente")
colegio.get(cambio)
colegio.update({cambio:nuevoValor})
cambio=input("Indique la asignatura a la que quiere editar el docente: ")
nuevoValor= input("Indique el nuevo nombre del docente")
colegio.get(cambio)
colegio.update({cambio:nuevoValor})
print(f"Asi quedo editada la lista con los nuevos docentes: {colegio}")

# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor
# listaNum =[]
# numUser= int(input("Ingrese numeros, para finalizar ingrese [0]: "))

# while numUser !=0:
#     listaNum.append(numUser)
#     numUser= int(input("Ingrese numeros, para finalizar ingrese [0]: "))
#     print(listaNum)
#     listaNum.sort(reverse=True)
# print(f"Lista finalizada: {listaNum}")

# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero

# meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
# longitud= len(meses)

# numUser= int(input("Ingrese un numero del 1 al 12: "))

# if numUser<=longitud:
#     print(f"El mes selecionado es {meses[numUser-1]}")
# else:
#     print("Intente con un numero del 1 al 12")


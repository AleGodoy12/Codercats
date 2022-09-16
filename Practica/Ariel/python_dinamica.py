alumnos = [{'nombre': 'Ariel', 'altura': 170, 'grado': 1, 'curso': 'A'},
{'nombre': 'Azul', 'altura': 150, 'grado': 5, 'curso': 'C'}, {'nombre': 'Luja', 'altura': 160, 'grado': 5, 'curso': 'C'}]

def datos():
    nombre = input("Ingresa nombre del alumno: ").capitalize()
    altura = int(input("Ingresa altura del alumno: "))
    grado = int(input("Ingresa grado del alumno de 1 a 5: "))
    curso = input("Ingrese el curso del alumno A, B o C: ").capitalize()

    alumnos.append({"nombre": nombre, "altura": altura, "grado": grado, "curso": curso})

    operacion = input("Desea ingresar datos de un alumno [y/n]: ")
    if operacion == "y":     
        datos()
    elif operacion == "n":
        print("Operación terminada")

def posicion_y_nombre(lista):
    posicion = 1
    for x in lista:
        print("Alumno:", x["nombre"], ", posicion en fila:", str(posicion))
        posicion += 1

def cantidad_alumnos(lista):
    cursoA, cursoB, cursoC = 0, 0, 0
    for x in lista:
        if x["curso"] == "A":
            cursoA += 1
        elif x["curso"] == "B":
            cursoB += 1
        elif x["curso"] == "C":
            cursoC += 1
    return cursoA, cursoB, cursoC

def altura_segun_grado(lista, grado):
    posicion = 1
    mayor = 0
    posicionMayor, posicionMenor = 0, 0  
    menor = alumnos[0]["altura"]
    for x in lista:
        if x["grado"] == grado:
            if x["altura"] > mayor:
                mayor = x["altura"]
                posicionMayor = posicion
            if x["altura"] < menor:
                menor = x["altura"]
                posicionMenor = posicion
        posicion += 1
    return mayor, posicionMayor, menor, posicionMenor

def promedio_altura(lista):
    sumaAlturas = 0
    for x in lista:
        sumaAlturas += x["altura"]
    promedio = sumaAlturas / len(alumnos)
    return promedio

datos()

posicion_y_nombre(alumnos)

cursoA, cursoB, cursoC = cantidad_alumnos(alumnos)

mayor, posicionMayor, menor, posicionMenor = altura_segun_grado(alumnos, 5)

promedio = promedio_altura(alumnos)

print(f"""
Del curso A hay: {cursoA} alumnos
Del curso B hay: {cursoB} alumnos
Del curso C hay: {cursoC} alumnos
""")

print(f"La mayor altura de quinto grado es: {mayor}, posicion: {posicionMayor} y menor altura: {menor}, posicion: {posicionMenor}")

print(f"La altura promedio es: {promedio}")
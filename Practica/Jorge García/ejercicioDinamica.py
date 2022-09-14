import os

def contarCantidadCurso(listaAlumnos, curso):
    cantidad = 0  
    for alumno in listaAlumnos:
        if(alumno["Curso"] == curso):
            cantidad += 1
    return cantidad

def calcularPromAltura(listaAlumnos):
    acumAltura = 0  
    for alumno in listaAlumnos:
        acumAltura += alumno["Altura"]
    return acumAltura/len(listaAlumnos)

def obtenerAlumnoMasAlto(listaAlumnos):
    alturaMax = 0
    alumnoMax = None
    for alumno in listaAlumnos:
        if(alumno["Altura"] > alturaMax and alumno["Grado"] == 5):
            alumnoMax = alumno
            alturaMax = alumno["Altura"]
    return alumnoMax

def obtenerAlumnoMasBajo(listaAlumnos):
    alturaMin = obtenerAlumnoMasAlto(listaAlumnos)['Altura']
    alumnoMin = None
    for alumno in listaAlumnos:
        if(alumno["Altura"] < alturaMin and alumno["Grado"] == 5):
            alumnoMin = alumno
            alturaMin = alumno["Altura"]
    return alumnoMin

def agregarAlumno(listaAlumnos, cursos, grados):
    nombre = input("Nombre: ").capitalize()
    try:
        altura = int(input("Altura: "))
        grado = int(input("Grado [1-5]: "))
    except:
        print("¡Error en los datos numéricos! Inténtalo de nuevo.")
        return False
    curso = input("Curso [A-B-C]: ").upper()
    if(grado in grados and curso in cursos):
        listaAlumnos.append({'Nombre': nombre, 'Altura': altura, 'Grado': grado, 'Curso': curso})
        os.system("cls")
        return True
    else:
        print("Grado o curso inválido")
    return False

cursos = ["A", "B", "C"]
grados = [x for x in range(1, 6)]
listaAlumnos = [{"Nombre": "Pepe", "Altura": 150, "Grado": 5, "Curso":"A"},
                {"Nombre": "Ale", "Altura": 190, "Grado": 5, "Curso":"B"},
                {"Nombre": "Maria", "Altura": 170, "Grado": 5, "Curso":"A"}]

respuesta = None
os.system("cls")
while respuesta != "no":
    if agregarAlumno(listaAlumnos, cursos, grados):
        print("¡Alumno agregado!")
    respuesta = input("¿Desea ingresar otro alumno [si/no]?: ").lower()
    os.system("cls")

# Consulta a)
print("\nCONSULTA A\n")
for alumno in listaAlumnos:
    print(f"Nombre: {alumno['Nombre']} - Posición: {listaAlumnos.index(alumno)+1}")

# Consulta b)
print("\nCONSULTA B\n")
for curso in cursos:
    print(f"Cantidad de alumnos en el curso {curso}: {contarCantidadCurso(listaAlumnos, curso)}")

# Consulta c)
print("\nCONSULTA C\n")
alumnoAlto = obtenerAlumnoMasAlto(listaAlumnos)
alumnoBajo = obtenerAlumnoMasBajo(listaAlumnos)
print(f"Altura del alumno más alto de 5to grado: {alumnoAlto['Altura']} cm - Posición en la fila: {listaAlumnos.index(alumnoAlto)+1}")
print(f"\nAltura del alumno más bajo de 5to grado: {alumnoBajo['Altura']} cm - Posición en la fila: {listaAlumnos.index(alumnoBajo)+1}")

# Consulta d)
print("\nCONSULTA D\n")
print(f"Promedio de altura: {calcularPromAltura(listaAlumnos)} cm\n")

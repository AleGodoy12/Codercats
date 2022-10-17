#Alumnos que ya estaban en la fila
alumnos = [
    ("Abril",5,"A",170),
    ("Florencia",5,"A",165),
    ("Lujan",5,"A",160),
    ("Lucas",5,"B",174),
    ("Ariel",3,"B",180),
    ("Alejandro",4,"C",173)
]

#Modulos
def agregarAlumno():
    nombre= input("Ingrese el nombre del alumno: ").capitalize()
    grado = int(input("Ingrese el grado del alumno: "))
    curso = input("Ingrese el curso del alumno(A B o C): ").capitalize()
    altura = int(input("Ingrese la altura del alumno [cm]: "))
    datos = (nombre,grado,curso,altura)
    alumnos.append(datos)
    confirmacion = input("Desea seguir agregando alumnos? [si/no]: ").lower()
    if confirmacion == "si":
        agregarAlumno()
    else:
        print (alumnos)

def cantAlumnos():
    grado=int(input("Ingrese el grado: "))
    curso=input("Ingrese un curso (A B o C): ").capitalize()
    acumulador=0
    for alumno in alumnos:
        if grado==alumno[1] and curso == alumno[2]:
            acumulador+=1
    print("La cantidad de alumnos en el curso son:", acumulador)

def alumnoAlto():
    alturas=[]
    for alumno in alumnos:
        if alumno[1]==5:
            alturas.append(alumno[3])
    altura=max(alturas)
    for alumno in alumnos:
        if alumno[1]==5 and alumno[3]==altura:
            posicion=alumnos.index(alumno)
    print("El alumno más alto (de 5to) mide ",altura," y se encuentra en la posicion",posicion)
    
def alumnoBajo():
    alturas=[]
    for alumno in alumnos:
        if alumno[1]==5:
            alturas.append(alumno[3])
    altura=min(alturas)
    for alumno in alumnos:
        if alumno[1]==5 and alumno[3]==altura:
            posicion=alumnos.index(alumno)
    print("El alumno más bajo (de 5to) mide:",altura," y se encuentra en la posicion",posicion) 

def promedioAltura():
    alturas=[]
    for alumno in alumnos:
        alturas.append(alumno[3])
    promedio=sum(alturas)/len(alturas)
    print("El promedio de altura es:",promedio)  

#Ejecucion de la app
menu=None
while menu !="F":
    menu= input("\n      --- Menú ---\n[A] Agregar alumnos\n[B] Cantidad de alumnos por curso\n[C] Alumno más alto\n[D] Alumno más bajo\n[E] Promedio alturas\n[F] Salir\nOpción: ").capitalize()
    if menu=="A":
        agregarAlumno()
    elif menu=="B":
        cantAlumnos()
    elif menu=="C":
        alumnoAlto()
    elif menu=="D":
        alumnoBajo()
    elif menu=="E":
        promedioAltura()
print("Usted ha finalizado")

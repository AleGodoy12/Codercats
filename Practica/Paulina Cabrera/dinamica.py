#agregar alumnos hasta que el usuario desea

alumnos = [('pedro', 5, 125, 'C'), ('Juan', 5, 125, 'B'), 
           ("juana", 5, 130, "B"), ("David", 5, 130, "A"),
           ("Oriana", 5, 148, "A"), ("Luca", 5, 150, "C")]
def agregaralumno():
    nombre= input("Ingrese el nombre del alumno: ")
    grado = int(input("Ingrese el grado del alumno: "))
    altura = int(input("Ingrese la altura del alumno: 'FORMATO CM' [ej. 1.50 = 150]"))
    curso = input("Ingrese el curso del alumno [A, B, C]: ").capitalize()
    datos = (nombre,grado,altura,curso)
    alumnos.append(datos)
    confirmacion = input("¿Desea seguir agregando alumnos? [S/N]").capitalize()
    if confirmacion == "S":
        agregaralumno()
    else:
         print("Alumnos agregados")
         print (alumnos)

agregaralumno()

#Cantidad de alumnos
def cantAlumnos():
    grado=int(input("Ingrese el grado: "))
    curso=input("Ingrese un curso [A, B, C]: ").capitalize()
    acumulador=0
    for alumno in alumnos:
        if grado==alumno[1] and curso == alumno[3]:
            acumulador+=1
    print(f"La cantidad de alumnos en el curso {grado}° {curso} son: {acumulador}")
print(cantAlumnos())

def alturaMaxyMin():
    altMax= []
    grado=int(input("Ingrese el grado: "))
    if grado != 5:
        print("Solo puede averiguar las alturas de los alumnos de 5°")
    elif grado==5:
        for alumno in alumnos:   
            altMax.append(alumno[2])
            maximo= max(altMax)
            minimo= min(altMax)
            print(f"La altura maxima de 5° es {maximo} y la altura minima es {minimo}")
            
print(alturaMaxyMin())

def promedio():
    contador = 0
    for altura in alumnos:
        contador += altura[2]
    promedioFinal = contador / len(alumnos)
    print(f"El promedio de altura de los alumnos es igual a : {promedioFinal}") 

print(promedio())

def posicionFila():
    for posicion in alumnos:
        print(f"El alumno {posicion[0]} de {posicion[1]}° se encuentra en la posicion {alumnos.index(posicion)+1} de la fila")
print(posicionFila())

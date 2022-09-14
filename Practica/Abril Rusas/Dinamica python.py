lista = []
def agregarAlumno():
    nombre= input("ingrese el nombre del alumno: ")
    grado = int(input("ingrese el grado del alumno: "))
    altura = float(input("ingrese la altura del alumno: "))
    curso = input("ingrese el curso del alumno(A B o C): ").capitalize()
    datos = (nombre,grado,altura,curso)
    lista.append(datos)
    confirmacion = input("desea seguir agregando alumnos? [si/no]: ")
    if confirmacion == "si":
        agregarAlumno()
    elif confirmacion == "no":
        print (lista)
    else:
        print("Error, debe ingresar si o no")

agregarAlumno()
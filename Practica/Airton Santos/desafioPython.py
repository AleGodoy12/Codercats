import math 

def ingresoAlumnos():
    
    listaAlumnos = []
    listaAlturas = []
    
    verificacion = input("Desea ingresar registros?[S/N]")

    while verificacion == "S":

        nombre = input ("Ingrese su nombre")
        altura = float(input("Ingrese su altura"))
        grado = int(input("Ingrese el grado"))
        curso = input("Ingrese el curso [A/B/C]")

        tuplaAlumnos = (nombre, altura, grado, curso)
        listaAlumnos.append(tuplaAlumnos)

        for i in listaAlumnos:
            print(f"Alumno/a ingresado/a es:", i[0],". Su posición en la fila es:", (listaAlumnos.index(i)+1))

        verificacion = input("Desea ingresar registros?[S/N]")

    else: 
        for i in listaAlumnos:

            listaAlturas.append(i[1])
            promedioAlturas = math.fsum(listaAlturas)/len(listaAlturas)

            if i[2] == 5:
            
                alturaMimina = min(listaAlturas)
                alturaMaxima = max(listaAlturas)


        print(f"La altura maxima es:", alturaMaxima, "Su posición en la fila es la número: ",  (listaAlturas.index(alturaMaxima)+1 ))
        print(f"La altura mínima es:", alturaMimina, "Su posición en la fila es la número: ",  (listaAlturas.index(alturaMimina) +1))
        print("El promedio de altura de todos los cursos es de:", promedioAlturas)

ingresoAlumnos()

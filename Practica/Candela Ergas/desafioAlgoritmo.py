#Defino la variable alumnos para guardar los datos de los alumnos en una lista.
alumnos = [
    ["Morena",160,3,"B"],
    ["Violeta",155,5,"C"],
    ["Federico",181,1,"B"],
    ["Francisco",175,5,"A"],
    ["Julieta",170,5,"C"]
    ]

def agregarAlumno():
    #Defino las variables donde voy a pedir cada dato que se quiera ingresar.
    nombre= input("Ingrese el nombre del alumno: ").capitalize()
    altura = int(input("Ingrese la altura del alumno (en cm,SIN comas ni puntos): "))
    grado = int(input("Ingrese el grado del alumno (1,2,3,4 o 5): "))
    curso = input("Ingrese el curso del alumno(A B o C): ").capitalize()

    #Guardo esos datos de manera ordenada en una lista.
    datos = [nombre,altura,grado,curso]

    #Agrego esa lista a la original donde ya existen datos de alumnos.
    alumnos.append(datos)

    #Pregunto si quiere agregar más alumnos, si ingresa "y" vuelve a pedir datos, si ingresa otra cosa muestra la lista de los alumnos y sus datos.
    confirmacion = input("\nAgregado! Desea agregar más alumnos? [s/n] : \n").lower()
    if confirmacion == "s":
        agregarAlumno()
    else:
        print(f"Ok!")
#agregarAlumno()

def posicion():
    #Recorro la lista de alumnos,obtengo su nombre con el indice 0 y uso el método index para sumarle 1 al resultado y obtener su posición en la fila.
    for alumno in alumnos:
        print(f" {alumno[0]} se encuentra en el lugar nro {alumnos.index(alumno)+1} de la fila")
#posicion()

def cantCurso():
    #Guardo en dos variables los datos que ingresan para grado y curso.
    grado=int(input("\nIngresá el grado (1,2,3,4 o 5) : "))
    curso=input("\nIngresá el curso(A,B o C) : ").capitalize()

    #Defino una variable en 0 para utilarla de acumulador.
    totalAlumnos=0

    #Recorro la lista alumnos, por cada alumno que cumple con las condiciones incremento 1 el total de alumnos para ese curso.
    for alumno in alumnos:
        if alumno[2]==grado and alumno[3]==curso:
            totalAlumnos+=1
    
    #Si el total es mayor a 0 indico cuantos alumnos hay de ese grado, sino indico que no hay ninguno.
    if totalAlumnos>0:
        print(f"\n En la fila del curso {grado} {curso} hay {totalAlumnos} alumno/s ")
    else:
        print("\n No hay alumnos de ese curso")
    seguir=input("\nQuerés ver otro curso? [s/n] : ")
    if seguir=="s":
        cantCurso()
    else:
        print("\nPerfecto! Seguimos :)")
#cantCurso()

def alturas():
    #Defino la variable alto como una lista de 3 elementos: el 1ro para guardar el nombre,el 2do para guardar la altura y el 3ro para guardar la ubicacion en la fila.
    alto=["",0,0]

    #Itero en la lista alumnos para analizar cada elemento de la misma y saber cual cumple las condiciones dadas para guardar sus datos en la variable alto.
    for alumno in alumnos:
        if alumno[2]==5 and alumno[1]>alto[1]:
            #Busca el indice y del alumno que estoy analizando y sumo 1 para saber su lugar en la lista de alumnos
            fila=alumnos.index(alumno)+1 
            #Asigno a la variable alto los valores del alumno actual para que los compare con los del siguiente alumno
            alto= [alumno[0],alumno[1],fila] 

    #Defino la variable bajo al igual que alto, pero tomando como parámetro inicial de altura(2do parámetro),la altura máxima obtenida anteriormente.
    bajo=["",alto[1],0]
    for alumno in alumnos:
        if alumno[2]==5 and alumno[1]<bajo[1]:
            fila=alumnos.index(alumno)+1
            bajo= [alumno[0],alumno[1],fila]

    #Imprimo los datos del alumno más alto y el más bajo.
    print(f"\nEl/la más alto/a de 5to es {alto[0]}, mide {alto[1]}cm y está ubicado/a en el lugar {alto[2]} de la fila. ")
    print(f"El/la más bajo/a de 5to es {bajo[0]}, mide {bajo[1]}cm y está ubicado/a en el lugar {bajo[2]} de la fila. ")
#alturas()

def promedioAlturas():
    #Defino una lista vacia para almacenar las alturas
    alturas=[]

    #Recorro la lista para obtener la altura de cada alumno y agregarla a la lista.
    for alumno in alumnos:
        alturas.append(alumno[1])

    #Defino la variable promedio donde sumo las alturas y lo divido por la cantidad de elementos de esa lista. Luego lo muestro por pantalla
    promedio= sum(alturas) / len(alturas)
    
    print(f"\nEl promedio de alturas entre los alumnos de todos los cursos es de {round(promedio,2)} cm. ")
#promedioAlturas()

def aplicacion():
    print(f"Estos son son los alumnos que hay actualmente: \n {alumnos}\n ")
    posicion()
    print("\nTambién podés ver la cantidad de alumnos en cada curso individualmente!")
    cantCurso()
    alturas()
    promedioAlturas()
    confirmacion = input("\nYa viste todos los datos disponibles! Querés agregar más alumnos? [s/n] : ").lower()
    if confirmacion == "s":
        agregarAlumno()
        print("\nYa agregamos los alumnos que querias, vamos a ver los datos actualizados!\n ")
        aplicacion()
    else:
        print("\nTerminamos, gracias!")
aplicacion()


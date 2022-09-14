alumnos = {}

while True:
    operacion = input("Desea ingresar datos de un alumno [y/n]: ")
    if operacion == "y":     
        nombre = input("Ingresa nombre del alumno: ")
        altura = float(input("Ingresa altura del alumno: "))

        grado = int(input("Ingresa grado del alumno: "))
        if (grado <1 or grado > 5):
            grado = input('Los grados existentes son del 1 al 5')
        else: 
            curso = input("Ingrese el curso del alumno: ").capitalize()
            if(curso != "A" and curso != "B" and curso != "C"):
                cuso = input('Los grados existentes son A, B o C').capitalize()
            else:
                alumnos.update({"nombre": nombre, "altura": altura, "grado": grado, "curso": curso})
                print(alumnos)
    elif operacion == "n":
        print("Operación terminada")
        break
    else:
        operacion = input("Desea ingresar datos de un alumno [y/n]: ")
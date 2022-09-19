from pickletools import decimalnl_long
import numpy as np

# Para probar los ejercicios a partir del n°2
# alumnos = [
#     {'nombre': 'lujan', 'altura': 1.7, 'grado': 3, 'curso': 'A'}, 
#     {'nombre': 'gaston', 'altura': 1.8, 'grado': 4, 'curso': 'A'}, 
#     {'nombre': 'ale', 'altura': 1.6, 'grado': 3, 'curso': 'A'}, 
#     {'nombre': 'brishito', 'altura': 1.1, 'grado': 3, 'curso': 'C'},
#     {'nombre': 'mayra', 'altura': 1.5, 'grado': 5, 'curso': 'B'},
#     {'nombre': 'stella', 'altura': 1.4, 'grado': 2, 'curso': 'B'},
#     {'nombre': 'micaela', 'altura': 1.6, 'grado': 5, 'curso': 'A'},
#     {'nombre': 'carla', 'altura': 1.7, 'grado': 5, 'curso': 'C'},
#     ]

alumnos = []
def colegio ():
    while True:
        operacion = input("Desea ingresar datos de un alumno [y/n]: ")
        if operacion == "y":     
            nombre = input("Ingresa nombre del alumno: ").capitalize()
            altura = float(input("Ingresa altura del alumno: "))
            grado = int(input("Ingresa grado del alumno: "))
            if (grado <1 or grado > 5):
                grado = input('Los grados existentes son del 1 al 5')
            else: 
                curso = input("Ingrese el curso del alumno: ").capitalize()
                if(curso != "A" and curso != "B" and curso != "C"):
                    cuso = input('Los grados existentes son A, B o C').capitalize()
                else:
                    alumnos.append({"nombre": nombre, "altura": altura, "grado": grado, "curso": curso})
 
                print(alumnos)
                
        elif operacion == "n":
            print("Operación terminada")
            break
        else:
            operacion = input("Desea ingresar datos de un alumno [y/n]: ")
colegio()

def informe(alumnos):
    i = 0
    for alumno in alumnos:
        print(alumno['nombre'], i)
        i +=1
informe(alumnos)

def alumnosxcurso(alumnos):
    a = 0
    b = 0
    c = 0
    for alumno in alumnos:
        if alumno['curso'] == "A":
            a += 1
        elif alumno['curso'] == "B":
            b += 1
        elif alumno['curso'] == "C":
            c += 1
    print('Curso A:' , a , '\n Curso B:' , b ,'\n Curso C: ', c)

alumnosxcurso(alumnos)

def minMaxAltura (alumnos):
    agregando = []
    alumno = 0
    for alumno in alumnos:
        if alumno['grado'] == 5:
            altura = alumno.get('altura')
            agregando.append(altura)
    print('La mínima altura es', min(agregando), 'y la máxima altura es', max(agregando))
            
minMaxAltura(alumnos)

def promedio (alumnos):
    alturaArr = []
    for alumno in alumnos:
        altura = alumno.get('altura')
        alturaArr.append(altura)
        promedio = np.mean(alturaArr)
    print('El promedio de las alturas es:', '{:.2f}'.format(promedio))  
promedio(alumnos)





#1
def diferencia (num1, num2):
    for i in range(num1, num2):
        print(i + 1) 

diferencia(1, 15)

#2
def validacion (dni):
    if len(dni) == 8 or len(dni) == 7:
        print('Es válido')
    else:
        print('Es inválido')
validacion('41127645')

#3
def datos ():
    nombre = 'Luján'
    colorFavorito = 'verde'
    print('Mi nombre es' , nombre , 'y mi color favorito es' , colorFavorito)

datos()

# Y para que sea reutilizable
nombre = input('Ingresá tu nombre')
colorFavorito = input('Ingrespa tu color favorito')
def datos (nombre, colorFav):
   print('Mi nombre es' , nombre , 'y mi color favorito es' , colorFav)
datos(nombre, colorFavorito)

#Lujan, increible el crecimiento en estas ultimas dos semanas, va de la mano del compromiso, el empeño
#y las ganas de llegar al objetivo, vas avanzando ademas de bien, solido y eso es lo que mas valoro!
#Muy buenas las dos resoluciones del codigo, ambas formas validas y de pocas lineas de codigo, genial la manera de enfocarlo!
#10/10

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
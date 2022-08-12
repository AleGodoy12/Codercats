#1
meses = (0 , 'Enero' , 'Febrero', 'Marzo' , 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
usuario = int(input('Dame un numero '))
while (usuario != 0):
    i = 0
    if (i <= len(meses)):
        print(meses[usuario])
    else:
        print('Error')
    usuario = int(input('Dame un numero '))
    print('Fin')

#2
numeros = (1,1,2,4,5,8,5,7,7,6,5,2,4,7,1,8,1,1,7,7,6,5,4,3,2,2,4,6,6,7,8,9,9,9,9,0,0,9,8,7,6,5,4,3,2,2,3,4,4,5,6,7,8,8,7,6,4)
usuario = int(input('Dame un numero del 1 al 9 '))
print(numeros.count(usuario))

#3 
numeros = (1,2,3,4,5,6,7,8,9,10)
usuario = int(input('Dame un numero del 1 al 10 '))
print(numeros.index(usuario +1))
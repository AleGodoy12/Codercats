meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
numUsuario = int(input('Ingresá un numero'))
while numUsuario != 0:
    if numUsuario < len(meses):
        print(meses[numUsuario -1])
        break
    else: 
        print('Error')   
        break 
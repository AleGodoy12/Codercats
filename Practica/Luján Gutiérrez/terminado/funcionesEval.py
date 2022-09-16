#1
def parImpar (num):
    if (num % 2 != 0 ):
        print('Es impar')
    else:
        print('Es par')

parImpar(4)

#2
def distancia (num1, num2):
    for i in range(num1, num2):
        print(i)


#3

def validacion ():
    DNI = str(input('Ingresá tu DNI'))
    if (len(DNI) >= 7 or len(DNI) <= 8):
        print ('Es válido')
    else:
        print ('Es invalido, el DNI debe contener entre 7 y 8 dígitos')
validacion()

#4
def ultimaPalabra (string):
    
    def funcion (a,b,c=[]):
    if a==b:
        c.append(a)
        print(c)
        return c
    elif 
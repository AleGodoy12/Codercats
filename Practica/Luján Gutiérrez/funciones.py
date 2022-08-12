#1
mail = str(input('Ingresá tu mail '))
i = 0
def esValido(mail):
    for i in mail:
        if '@' in mail:
            return 'Es valido'
        else: 
            return 'Es invalido'
print(esValido(mail))

#2

def sumDig ():
    numero = str(input ('Ingresá un número'))
    acc = 0
    while (numero != "0"):
        for i in numero:
            acc += int(i) #acá me suma el primer digito con el segundo y me los guarda en la variable suma
        print (acc)
        acc = 0 #esto resetea la variable acumuladora
        numero = str(input ('Ingresá un número'))
sumDig()

#3




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
numero = input('Ingresá un numero')
i = 0
def numero (num):
    while (num != 0):
        i += num
        i += 1
        return i 
    
num = 'numero'
digitos = []
def numero (num):
    num = int(input('Ingresa un numero'))
    i = 0
    for i in num:
        digitos.append(i)
    sum(digitos)
    return digitos

numero(num)
print(numero(num))
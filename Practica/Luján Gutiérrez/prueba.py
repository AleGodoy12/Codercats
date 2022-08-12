def sumDig ():
    numero = str(input('Ingresá un número '))
    suma = []
    acc = 0
    while (numero != "0"):
        suma.append(numero)
        for i in numero:
            acc += int(i) #acá me suma el primer digito con el segundo y me los guarda en la variable suma
        print (acc)
        acc = 0 #esto resetea la variable acumuladora
        numero = str(input('Ingresá un número '))
    print(eval(suma))
sumDig()


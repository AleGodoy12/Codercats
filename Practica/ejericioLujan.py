lista = []
def listaNumeros():
    numeros = input('Ingresá un número')
    while numeros != "0":
        lista.append(numeros)
        numeros = input('Ingresá un número')
    print(lista)
    lista.sort()
    lista.reverse()
    print('De mayor a menor', lista)
listaNumeros()

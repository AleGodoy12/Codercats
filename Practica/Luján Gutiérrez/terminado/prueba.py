dicc = {}

def contando ():
    arr = [5,16,2,5,57,5,2]
    for i in arr:
        if i not in dicc:
            veces = arr.count(i)
            dicc.update({i:veces})
    print(dicc)
contando()
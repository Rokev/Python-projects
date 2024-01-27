#Determina temperatura max y min de una lista, si es negativa se debe imprimir al finalizar, la lista finaliza con un 0. sumar las positivas y negativas

temperaturas=[25, 34, -8, 16, -22, -30, 0]
print(temperaturas)

def mayor(lista):
    max = lista[0],
    for x in lista:
        if x > max:
            max = x
    return max    

def menor(lista):
    min = lista[0],
    for x in lista:
        if x < min:
            min = x
    return min
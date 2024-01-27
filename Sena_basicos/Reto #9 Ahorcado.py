#Reto 9

import random
import os

palabras= ['MAÑANA', 'CHOCOLATE', 'SABADO', 'MANZANA', 'ALGORITMOS', 'ASTRALOPITECUS', 
        'BOTELLA', 'PAPEL', 'SUDOKU', 'DOCTOR', 'MILITAR', 'ASTEROIDE', 'SUERTE', 'MATERIALES' ]

palabra = list(random.choice(palabras))

horca= ['               !=======N',
        '                       N',
        '                       N',
        '                       N',
        '                       N',
        '                       N',
        '                       N',
        '           ____________N',]

ahorcado= ['               !=======N',
        '               O       N',
        '             | | |     N',
        '               |       N',
        '               |       N',
        '             |   |     N',
        '             |   |     N',
        '           ____________N',]

letras_todas=[]
fallos=1

resultado=[]

for i in range(len(palabra)):
    resultado.append('_')


while True:

    os.system('cls')

    print("***   JUEGO DEL AHORCADO   ***")
    print("******************************")
    for i in range(fallos):
        print(ahorcado[1])
    for i in range(len(horca)-fallos):
        print(horca[i+fallos])

    print()


    print("     ", end=" ")
    for i in resultado:
        print(i, end=" ")
    
    print()
    print()


    if resultado== palabra:
        print("***       HAS GANADO       ***")
        break

    if fallos > 6:
        print('la palabra era:', "".join(palabra))
        print('***       HAS PERDIDO       ***')
        break

    #Bucle para la seleccion de palabras

    while True:
        letra_usuario_sin_fprmato=input('Dime una letra: ')
        letra_usuario= letra_usuario_sin_fprmato.upper
        if len(letra_usuario) !=1:
            print('introduce una letra')
        elif letra_usuario in letras_todas:
            print('Esta letra ya la has dicho')
        elif letra_usuario not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('introduce una letra')
        else:
            letras_todas.append(letra_usuario)
            break

    #comprobamos si la letra esta en la palabra

    for i in range(len(palabra)):
        if palabra[i] == letra_usuario:
            resultado[i]= letra_usuario
    if letra_usuario not in palabra:
        fallos += 1

    print()
    print()
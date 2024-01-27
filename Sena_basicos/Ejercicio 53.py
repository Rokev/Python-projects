while True:
    valor_ingresado= int(input('ingrese un numero entero: '))
    if valor_ingresado % 2 != 0:
        print('este es un numero impar')
        break
    print('este es un numero par')
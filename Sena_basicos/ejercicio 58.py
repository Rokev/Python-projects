#Programa que escoja entre Hombre o mujer y que diga bienvenido(a) dependendiendo de lo ingresado.

print('1) Masculino',
            '2) Femenino',
            '3) Otro genero',)
Genero=input('Seleccione su genero:')

if Genero == '1':
    print('Bienvenido!')
elif Genero=='2':
    print('Bienvenida!')
elif Genero=='3':
    print("Bienvenide?")
else:
    print('Por favor, seleccione una de las opciones indicadas')
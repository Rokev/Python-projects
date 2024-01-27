# Determinar el area y perimetro de un rectangulo cuyas dimensiones se lean desde el teclado

Lado1= int(input('ingrese el largo del rectangulo: '))
lado2= int(input('ingrese el ancho del rectangulo: '))

Area= lado2*Lado1
Perimetro= lado2*2 + Lado1*2

if lado2 <= 0:
    print("por favor digite un valor natural positivo diferente de 0")
if Lado1<= 0:
    print("por favor digite un valor natural positivo diferente de 0")

print(f"el el area del rectangulo es {Area} y el perimetro del rectangulo es {Perimetro}")





#Realizar una aplicación que calcule las cuatro operaciones básicas, suma, resta, división, multiplicación, con dos números.

n1=float(input("ingrese el primer numero: "))
n2=float(input("ingrese el segundo numero: "))

option=0
while True:
    print(""" 
    Dime, que quieres hacer?
    1) sumar los dos numeros
    2) restar los dos numeros
    3) multiplicar los dos numeros
    4) dividir los dos numeros
    5) cambiar los numeros
    6) apagar la calcuadora
    """)
    option= float(input("Elige una opcion: "))

    if option == 1:
        print(" ")
        print("RESULTADO: la suma de", n1, "+",n2, "es igual aL: ", n1+n2)
    elif option == 2:
        print(" ")
        print("RESULTADO: la resta de ", n1, "-",n2, "es igual a: ", n1-n2)
    elif option == 3:
        print(" ")
        print("RESULTADO: la multiplicacion de ", n1, "*", n2, "es igual a: ", n1*n2)
    elif option == 4:
        print(" ")
        print("RESULTADO: la division de ",n1, "/", n2, "es igual a: ", n1/n2)
    elif option == 5:
        n1=float(input("Introduce tu primer numero: "))
        n2=float(input("Introduce tu segundo numero: "))     
    elif option == 6:
        break
    else:
        print("opcion incorrecta")






    
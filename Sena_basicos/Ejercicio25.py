#Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes si el banco paga a razón de 2% mensual.

print("Bienvenido al banco nacional de la republica! Estamos para servirle, diganos cuanto capital desea invertir y le diremos cuanto ganará en los proximos meses.")

capital=int(input("el capital es: "))

cantidad_meses= int(input("la cantidad de meses es: "))

dinero_ganado= (2*cantidad_meses)*(capital)/(100)

print(f"en {cantidad_meses} mes o meses usted habra ganadó: ", + dinero_ganado,)
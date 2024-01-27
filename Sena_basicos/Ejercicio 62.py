#Al cerrar un expendio de naranjas, n clientes que aún no han pagado recibirán un
#15% de descuento si compran más de 10 kilos. Determinar cuánto pagará cada cliente y cuanto
#percibirá la tienda por esas compras.


vn=float(input('Ingrese el valor de la naranja por kilo: ')) #10000
tc=float(input('Cuantos fueron los clientes que aun no han pagado?: ')) #10
print('Si algun cliente que aun no haya pagado desea recibir un 15 porciento de descuento, debera comprar mas de 10 kilos.')
cd=float(input('cuantos clientes compraran mas de 10 kilos?: '))  #2


if cd != 0:
    c1=float(input('Cuantos kilos comprara? : '))
    c2=float(input('Cuantos kilos comprara? : '))
    print('El total a pagar del cliente 1 sera de:' , c1)
    print('El total a pagar del cliente 2 sera de:' , c2)
    ganancia=(vn*(tc-cd))+(c1*vn*0.85)+(c2*vn*0.85)
    print('El total de dinero ganado por la tienda sera de:', ganancia)
else:
    print('el total de ganancia es de: ', tc*vn)



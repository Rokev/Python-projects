#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

#Para este ejercicio el sueldo base sera el minimo colombiano, 1160000 COP

sueldo_base=int(1160000)

comision= sueldo_base*10/100

cantidad_comision= int(input("Las comisiones al mes son: "))

extra_comision= comision*cantidad_comision

print("Las ganancias extra por comisiones son: ", extra_comision)

print("Y las ganancias totales del sueldo base y las comisiones son: ", sueldo_base+extra_comision)

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

#El cliente podra incluir hasta 7 productos
producto1=str(input("producto 1: "))
producto2=str(input("producto 2: "))
producto3=str(input("producto 3: "))
producto4=str(input("producto 4: "))
producto5=str(input("producto 5: "))
producto6=str(input("producto 6: "))
producto7=str(input("producto 7: "))

#El cliente podra incluir la cantidad de los productos
C_producto1=int(input(f"ingrese la cantidad del {producto1}: "))
C_producto2=int(input(f"ingrese la cantidad del {producto2}: "))
C_producto3=int(input(f"ingrese la cantidad del {producto3}: "))
C_producto4=int(input(f"ingrese la cantidad del {producto4}: "))
C_producto5=int(input(f"ingrese la cantidad del {producto5}: "))
C_producto6=int(input(f"ingrese la cantidad del {producto6}: "))
C_producto7=int(input(f"ingrese la cantidad del {producto7}: "))

#El cliente podra incluir el precio de cada producto
P_producto1=int(input(f"ingrese el precio del {producto1}: "))
P_producto2=int(input(f"ingrese el precio del {producto2}: "))
P_producto3=int(input(f"ingrese el precio del {producto3}: "))
P_producto4=int(input(f"ingrese el precio del {producto4}: "))
P_producto5=int(input(f"ingrese el precio del {producto5}: "))
P_producto6=int(input(f"ingrese el precio del {producto6}: "))
P_producto7=int(input(f"ingrese el precio del {producto7}: "))

Precio=(C_producto1*P_producto1)+(C_producto2*P_producto2)+(C_producto3*P_producto3)+(C_producto4*P_producto4)+(C_producto5*P_producto5)+(C_producto6*P_producto6)+(C_producto7*P_producto7)
print("El precio por todos los productos es: ", Precio)
Descuento=Precio*15/100
print("El descuento del 15 porciento sobre el precio es: ", Descuento)
Precio_Total=Precio-Descuento
print("El precio total a pagar es de: ", Precio_Total)

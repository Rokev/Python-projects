# Ingresando la cantidad de un producto y su precio unitario, obtener como resultado el precio final que debe pagar el cliente.

# El producto sera chocolatinas jet personal
cantidad=int(input("la cantidad de chocolatinas es: "))

precio=int(input("el precio unitario de las chocolatinas es: "))

precio_final=precio*cantidad

print(f"teniendo en cuenta de que tengo {cantidad} de chocolatinas, y su precio unitario es {precio}, yo pagare en total ", + precio_final, 'COP')


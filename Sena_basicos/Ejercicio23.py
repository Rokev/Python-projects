#Conociendo el valor de la entrada al cine, calcule el monto a pagar para una delegación de personas. Recuerde que deberá hacer un descuento del 3% por cantidad.

#El precio de la entrada sera en royal fimls un dia domingo para una pelicula en 2D
valor_entrada_cine=10500

personas= int(input("Cuantas personas van a ir? ")) 
print("Vamos a ir ", + personas, "personas")


valor_total= valor_entrada_cine*personas
descuento=valor_total*3/100

monto_total= valor_total-descuento

print(valor_total)
print(descuento)
print(monto_total)
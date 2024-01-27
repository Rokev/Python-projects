#crear un algoritmo que ordene la lista por tipo, tamaño y alegria navideña. Esto sin que se repitan 
lista_de_regalos = [
("Juguete", 5, 8),
("Libro de cuentos", 2, 6),
("Muñeco de nieve", 1, 9),
("Calcetines", 3, 4),
("Rompecabezas", 4, 7),
("Chocolate", 2, 5),
("Peluche", 5, 8),
("Juego de construcción", 3, 6),
("Galletas", 1, 7),
("Libro de cuentos", 2, 6),
("Peluche", 5, 8)
]
#Aca se eliminan los elementos repetidos
new_list=[]
for i in range(len(lista_de_regalos)):
    if lista_de_regalos[i] not in new_list:
                        new_list.append(lista_de_regalos[i])

##ste es el algoritmo por tipo, se organiza en orden alfabetico desde la A hasta la Z
new_list.sort() 
print(new_list)
#Me doy por vencido, perdon, en verdad queria organizar la lista por medio de los 3 digitos que se daban, pero despues de 3 horas me puede y ya no quiero hacerlo más.
#Intente con el metodo sorter con una key y lambda, hasta converti la lista en una tupla para ver si dejaba pero nada :(





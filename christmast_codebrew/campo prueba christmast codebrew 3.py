"""#en resuemn, crear un codigo que de regalos especificos a los miembros relevantes de la mafia del cafe.
#debe ser una cadena de regalos y algunos miembros tienen preferencias.

#en este caso importo la libreria random para que asi sea sorpresa a quien le toca dar y recibir regalos
import random 

#estos son los regalos, los saque de las cosas que los miembros no preferian y algunas cosas que mencionaba en la descripcion
regalos=["calcetines","codigo_php","chocolate","sueter","galletas","champagne","libros","tarjeta_regalo","reloj","peluche"]

#Aca creo las variables con el nombre de los miembros y aclaro que preferencia tiene 
miembros = [
    {"nombre": "Nikorasu", "evitar": "codigo_php"},
    {"nombre": "Dante", "evitar": "calcetines"},
    {"nombre": "Andestid", "evitar": "chocolates"},
    {"nombre": "Lost", "evitar": "Sin preferencias particulares"},
    {"nombre": "Mateo", "evitar": "champagne"},
    {"nombre": "Hannah", "evitar": "sueter"},
    {"nombre": "Lopez", "evitar": "galletas"},
    {"nombre": "Krasnay", "evitar": "reloj"},
    {"nombre": "Sword", "evitar": "Sin preferencias particulares"},
    {"nombre": "Caveira", "evitar": "peluche"}
]

#Aca hago que el orden de los miembros y los regalos sea aleatorio, para darle mayor suspenso a la hora de asignar regalos
random.shuffle(miembros)
random.shuffle(regalos)

#aca se asignan los regalos de cada participante y demas cosas
for i in range(len(miembros)):
    miembro_actual = miembros[i]
    regalo_actual = regalos[i]

    #aca evito que alguien reciba su mismo regalo
    while regalo_actual == miembro_actual["evitar"]:
        random.shuffle(regalos)
        regalo_actual = regalos[i]

    # Aca empieza la magia, pues se decide quien le dara un regalo a quien
    recibidor = miembros[(i + 1) % len(miembros)]

    #aca se le asigna el regalo al quien recibe el regalo
    miembro_actual["regalo_dado"] = regalo_actual
    recibidor["regalo_recibido"] = regalo_actual

    #y por ultimo se muestra quien le da a quien y que le da.
    print(f"{miembro_actual['nombre']} dará a {recibidor['nombre']}: {regalo_actual}")"""

# Ejemplo de dos listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 2, 1, 6]

# Comparar elemento por elemento
for valor1, valor2 in zip(lista1, lista2):
    if valor1 > valor2:
        print(f"{valor1} es mayor que {valor2}")
    elif valor1 < valor2:
        print(f"{valor1} es menor que {valor2}")
    else:
        print(f"{valor1} es igual a {valor2}")


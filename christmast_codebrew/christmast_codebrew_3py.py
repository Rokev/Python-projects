#en resuemn, crear un codigo que de regalos especificos a los miembros relevantes de la mafia del cafe.
#debe ser una cadena de regalos y algunos miembros tienen preferencias.

#en este caso importo la libreria random para que asi sea sorpresa a quien le toca dar y recibir regalos
import random 

#estos son los regalos, los saque de las cosas que los miembros no preferian y algunas cosas que mencionaba en la descripcion
regalos=["calcetines","codigo_php","chocolate","sueter","galletas","champagne","libros","tarjeta_regalo","reloj","peluche"]

#Aca creo las variables con el nombre de los miembros, (aunque en desorden, mala mia ahi) y les asigno un regalo para dar
nikorasu = random.choice(regalos)
regalos.remove(nikorasu)
sword = random.choice(regalos)
regalos.remove(sword)
mateo= random.choice(regalos)
regalos.remove(mateo)
hanna= random.choice(regalos)
regalos.remove(hanna)
dante= random.choice(regalos)
regalos.remove(dante)
andestid= random.choice(regalos)
regalos.remove(andestid)
lost= random.choice(regalos)
regalos.remove(lost)
lopez= random.choice(regalos)
regalos.remove(lopez)
krasnay= random.choice(regalos)
regalos.remove(krasnay)
caveira= random.choice(regalos)
regalos.remove(caveira)

#aca creo una variable que sirva de base para el intercambio de regalos con las variables anteriormente creadas
miembros=[nikorasu, dante, andestid, lost, mateo, hanna, lopez, krasnay, sword, caveira]

#con este print se puede ver que regalo tiene cada miembro (en este punto es el regalo que van a dar)
print("nikorasu da:",nikorasu,
        "\ndante da:", dante,
        "\nandestid da:",andestid,
        '\nlost da:',lost,
        "\nmateo da: ",mateo,
        "\nhanna da: ", hanna,
        '\nlopez da: ',lopez,
        '\nkrasnay da: ',krasnay,
        '\nsword da: ',sword,
        '\ncaveira da: ',caveira)

#esto es un salto de pagina
print()

#bueno, aca ocurre la magia en donde pues de manera aleatoria se van pasando los regalos.
#pero me di cuenta de que no logre la parte que evita que reciban lo que no quieren.
#Solo queda falta rezar para que todos obtengan algo que quieran....
while miembros != []:
    miembros=[nikorasu, dante, andestid, lost, mateo, hanna, lopez, krasnay, sword, caveira]
    if (nikorasu == nikorasu):
        nikorasu = random.choice(miembros,)
        miembros.remove(nikorasu)
    if (dante == dante) or (dante== "calcetines"):
        dante= random.choice(miembros)
        miembros.remove(dante)
    if (andestid == andestid) or (andestid== "chocolates"):
        andestid= random.choice(miembros)
        miembros.remove(andestid)
    if (lost == lost):
        lost= random.choice(miembros)
        miembros.remove(lost)
    if (mateo == mateo) or (mateo== "champagne"):
        mateo= random.choice(miembros)
        miembros.remove(mateo)
    if (hanna == hanna) or (hanna== "sueter"):
        hanna= random.choice(miembros)
        miembros.remove(hanna)
    if (lopez == lopez) or (lopez== "galletas"):
        lopez= random.choice(miembros)
        miembros.remove(lopez)
    if (krasnay == krasnay) or (krasnay== "reloj"):
        krasnay= random.choice(miembros)
        miembros.remove(krasnay)
    if (sword == sword):
        sword= random.choice(miembros)
        miembros.remove(sword)
    if (caveira == caveira) or (caveira== "peluche"):
        caveira= random.choice(miembros)
        miembros.remove(caveira)
    #aca se dice que recibe cada uno
    print("nikorasu recibe:",nikorasu,
        "\ndante recibe:", dante,
        "\nandestid recibe:",andestid,
        '\nlost recibe:',lost,
        "\nmateo recibe: ",mateo,
        "\nhanna recibe: ", hanna,
        '\nlopez recibe: ',lopez,
        '\nkrasnay recibe: ',krasnay,
        '\nsword recibe: ',sword,
        '\ncaveira recibe: ',caveira)



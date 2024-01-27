#el reto de hoy consiste en asignar al reno lider para santa, la competencia sera entre rodolfo y aurora quienes seran llamados 'a' y 'b'
#consiste en una serie de n pruebas en los cuales aquel que sea ganador de 3 consecutivas sera coronado.
#tambien se dan varias cosas interesantes, por ejemplo el consumo de energia en una serie de valores y caracteristicas extra, como res a la fatiga y asi.

#entiendo el reto como una comparacion entre el consumo de energia de ambos renos, y no quiero asignarles una cantidad especifica de energia
#en vez de eso hare que se comparen los consumos de energia y quien consuma menos va a ir ganando.

#Consumos de energía para el reno 'A': [12, 10, 9, 8, 12]
#Consumos de energía para el reno 'B': [11, 11, 9, 10, 13]
#Características únicas de 'A': [1, 2, 0, 1, 1]
#Características únicas de 'B': [0, 1, 2, 1, 0]


#Cree una funcion para que asi sea mas facil probar el codigo, asi solo tendran que cambiar los valores int de las listas y luego llamar a la funcion.
def ganador(consumo_a,consumo_b,caracteristicas_a,caracteristicas_b):
    #Las variables 'rodolfo' y 'aurora' sirven para que las caracteristicas unicas varien el valor del consumo de energia.
    # en este caso las caracteristicas unicas restan puntos al consumo para que el calculo se me haga mas facil.
    rodolfo = [val1 - val2 for val1, val2 in zip(consumo_a, caracteristicas_a)]
    aurora = [val1 - val2 for val1, val2 in zip(consumo_b, caracteristicas_b)]
    #las variables de victorias sirven para identificar quien consigue ser el ganador de 3 pruebas de manera consecutiva.
    victorias_a=0
    victorias_b=0
    #el ciclo while es para que el codigo funcione hasta que alguien consiga sus 3 victorias.
    while victorias_a!=3 or victorias_b!=3:
        # el for es para que la comparacion de consumo sea finita y termine en algun punto.
        for valor1, valor2 in zip(rodolfo, aurora):
            #este if y elif sirven para comparar el consumo de energia y aquel que consuma menos energia se lleva un punto.
            if valor2<valor1:
                victorias_b+=1
            elif valor1 < valor2:
                victorias_a+=1
            #por ultimo miramos quien es el ganador.
            if victorias_a == 3:
                return "El ganador es rodolfo"
            elif victorias_b==3:
                return"La ganadora es aurora"


consumo_a= [12, 10, 9, 8, 12]
consumo_b=[11, 11, 9, 10, 13]
#las caracteristicas seran: res a la fatiga, adaptabilidad, capacidad pulmonar, musculatura, astucia. 
caracteristicas_a=[1, 2, 0, 1, 1]
caracteristicas_b=[0, 1, 2, 1, 0]
resultado=ganador(consumo_a, consumo_b, caracteristicas_a, caracteristicas_b)
print(resultado)
#eso es todo, la verdad hoy no tuve un buen dia, no que digamos y eso se vio reflejado en que aunque tenia una idea mas o menos clara
#me demore unas 8 horas para poder terminar, hoy no tenia ganas de hacer nada, pero logre terminar el codigo en el mismo dia :D
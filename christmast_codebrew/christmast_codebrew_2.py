#Hoy toca Encuentro cosmico, 2 objetos con coordenadas y velocidades en un plano cartesiano.
#En resumen hay que crear un programa que nos diga en que punto sevan a encontrar ambos objetos.

#en esta funcion de abajo no programo como tal los objetos sino sus caracteristicas, como la posicion (x y y) y las velocidades (vx y vy) diferenciandolos por numeros 1 y 2.
def Encuentro_cosmico(x1,y1,vx1,vy1,x2,y2,vx2,vy2): 
    #el contador es para saber cuanto se demora en colicionar los objetos.
    contador=0
    #en este if verifico que no se formen lineas paralelas entre los objetos.
    if ((vx1 and vx2 == 0) and (vy1 and vy2 == 0)) or ((vx1==vx2) and (vy1==vy2)):
        return print("nunca se encontraran, es una trayectoria paralela")
    else:
        while x1 !=x2 or y1!=y2:
            x1=x1+vx1
            y1=y1+vy1
            x2=x2+vx2
            y2=y2+vy2
            contador=contador+1
    return print(f'Las coordenadas en las cuales los 2 objetos se van a encontrar son: {x1}, {y1} y se demora {contador} turnos')
#en estas variables se ponen los datos, siendo a y b las posiciones, va y vb las velocidades y el 1 y el 2 para diferenciar los objetos.
a1=0
b1=0
va1=2
vb1=3
a2=5
b2=5
va2=1
vb2=2
#se llama a la funcion y se le agregan los parametros.
Encuentro_cosmico(a1, b1, va1, vb1, a2, b2, va2, vb2)
#Y eso es todo, este me costo un poco, sobre todo el ciclo while y el condicional, hice varias pruebas propias y logre pasarlas, tambien me ayudaron a encontrar unos cuantos errores.
#Este reto si logre terminarlo! :D 
#aunque me demore bastante y encima empece a hacerlo tarde...

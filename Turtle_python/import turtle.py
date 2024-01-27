import turtle
import colorsys     

v=turtle.Screen()
v.bgcolor('black')
tortuga=turtle.Turtle()
tortuga.speed(0.5)
tortuga.color('blue')
iteraciones=100

for i in range(iteraciones*3):
    tortuga.forward(i*3)
    tortuga.right(200)
#para hacer un cuadrado poner right 90
#para hacer la estrella de 5 puntos poner right 145
#una figura que parece un circulo con 175
#una espiral recta con 45
#linea recta con 180
#140 un patron de estrellas que genera un patron de circulos
#120 piramide



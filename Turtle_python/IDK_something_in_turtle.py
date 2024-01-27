from turtle import*
import random
title("Practica")
bgcolor('black')

speed(0.5)

x=1
while x<500:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    right(889)
    x+=1


forward(500)



mainloop()
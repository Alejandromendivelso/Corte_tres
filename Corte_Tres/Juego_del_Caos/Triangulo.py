import turtle
import random

screen = turtle.Screen()
screen.title('juego del caos triangulo de sierpinski')
screen.setup(1000,1000)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

A = (0,350)
B = (-300,-200)
C = (300,-200)
V = (A,B,C)

for v in V:
    turtle.goto(v)
    turtle.dot('blue')

n = 10000 
p = (random.uniform(-200,200),random.uniform(-200,200)) 
t = turtle.Turtle()
t.up()
t.hideturtle()
for i in range(n):
    t.goto(p)
    t.dot(2,'red')
    r = random.randrange(len(V)) 
    p = ((V[r][0]+p[0])/2,(V[r][1]+p[1])/2)   
    if i % 1000 == 0: 
        t = turtle.Turtle() 
        t.up()
        t.hideturtle()
        screen.update()
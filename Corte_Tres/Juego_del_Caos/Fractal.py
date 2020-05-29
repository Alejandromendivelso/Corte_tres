import turtle
import random

ANG = 10      
RAND = 10   
REL = 4/5      
RANDT = 55    
GROSORTRONCO = 0   
TAMINIC = 100       
TAMHOJA = 8     
ANGHOJA = 60    
PROF = 8      

CTRONCO = (0,100,0)  
CTRONCOVAR = 40         
CHOJAS =  (255,90,109)  
CHOJASVAR = 100         
CFONDO = (0,0,0)  


def arbol(t, d):
    if d==0:
        turtle.forward(t)
        hoja(TAMHOJA, ANGHOJA)
        turtle.penup()
        turtle.back(t)
        turtle.pendown()
        turtle.color(CTRONCO)
        return
    else:
        angulo1 = ANG + random.randrange(-RAND, RAND+1)
        angulo2 = ANG + random.randrange(-RAND, RAND+1)
        tamano = t + t*random.randrange(-RANDT, RANDT+1)/100
        colortronco = variacioncolor(CTRONCO, CTRONCOVAR)
        turtle.color(colortronco)
        turtle.pensize(d+GROSORTRONCO)
        turtle.forward(tamano)
        turtle.left(angulo1)
        arbol(t*REL, d-1)
        turtle.right(angulo1+angulo2)
        arbol(t*REL, d-1)
        turtle.color(colortronco)
        turtle.left(angulo2)
        turtle.penup()
        turtle.back(tamano)
        turtle.pendown()


def hoja(t, a):
    turtle.color(variacioncolor(CHOJAS, CHOJASVAR))
    turtle.begin_fill()
    turtle.right(a/2)
    turtle.circle(t, a)
    turtle.left(180-a)
    turtle.circle(t, a)
    turtle.left(180-a/2)
    turtle.end_fill()


def variacioncolor(color, var):
    Rd = random.randrange(-var, var+1)
    Gd = random.randrange(-var, var+1)
    Bd = random.randrange(-var, var+1)
    R, G, B = color
    R += Rd
    G += Gd
    B += Bd
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return R, G, B

def init():
    turtle.speed(0)
    turtle.colormode(255)
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.back(200)
    turtle.pendown()
    turtle.hideturtle()
    turtle.color(CTRONCO)
    turtle.bgcolor(CFONDO)
    arbol(TAMINIC, PROF)
    turtle.done()

init()
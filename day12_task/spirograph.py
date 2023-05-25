# spirograph program
from turtle import Turtle,Screen
from random import randint
import turtle

circle_draw = Turtle()
turtle.colormode(255)
circle_draw.speed("normal")

# Function to obtain color
def color_circle():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

# Function to obtain size gap of spirograph
def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        circle_draw.color(color_circle())
        circle_draw.circle(100)
        circle_draw.setheading(circle_draw.heading() + 20)

draw_spirograph(10) 
show_circle = Screen()
show_circle.exitonclick()


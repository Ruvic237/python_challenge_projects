# Drawing a square using turtle
from turtle import Turtle,Screen
import random


# instance of the Turtle class
square = Turtle()
square.shape("turtle")
colors = ["green",'red',"yellow","blue"]
directions = [0,90,180,270]
square.pensize(15)
square.speed("normal")


# def draw_shape(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         square.forward(100)
#         square.right(angle)
  
        
# for shape_side in range(3,9):
#     square.color(random.choice(colors))
#     draw_shape(shape_side)
      
            
# random motion
for _ in range(200):
    square.color(random.choice(colors))
    square.forward(30)
    square.setheading(random.choice(directions))            
   
    
# for _ in range(10):
#     square.forward(10)
#     square.penup()
#     square.forward(10)
#     square.pendown()

    
# instance of Screen class
square_screen = Screen()
square_screen.exitonclick()




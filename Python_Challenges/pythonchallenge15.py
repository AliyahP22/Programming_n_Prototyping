#Aliyah P
#04-1-2025
#period 1
#Python coding challenge 15, which draws a koch snowflake using
#functions and if statements along with the turtle library

import turtle #library import needed
def koch_curve(t,length,depth):
  if length < 3:#checks if length is less than 3
    t.forward(length)#draws a straight line if condition is true
  else:#breaks into smaller segments
    koch_curve(t,length/3,depth-1)
    t.left(60)
    koch_curve(t,length/3,depth-1)
    t.right(120)
    koch_curve(t,length/3,depth-1)
    t.left(60)
    koch_curve(t,length/3,depth-1)
def draw_snowflake(t,length,depth):#function to draw snowflake
  for side in range(3):#runs loop 3 times for 3 sides
    koch_curve(t,length,depth)
    t.right(120)#turtle turns 120 degrees to form snowflake shape
    
pepito = turtle.Turtle() #turtle object defined
screen = turtle.Screen()
screen.bgcolor("white")#sets background color
pepito.speed(0)#sets to quickest speed
pepito.penup()
pepito.goto(-120,90)
pepito.pendown()
pepito.pencolor("blue")#changes color from black to blue
draw_snowflake(pepito,300,4)#call function


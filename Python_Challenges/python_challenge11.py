#Aliyah P
#Period 1
#03-22-2025
#Python Coding Challenge 11
import turtle
import math #neccesary imports needed
#initial code to draw tree
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length * n) 
    t.left(angle) 
    draw(t, length, n-1) 
    t.right(2 * angle)
    draw(t, length, n-1) 
    t.left(angle) 
    t.backward(length * n) 

def square(t, length):#initial code to draw square
    for sides in range(4):#runs loop 4 times for 4 sides
        t.forward(length)
        t.left(90)

def polygon(t, length, n):#define function to draw polygon with n as a parameter
    angle = 360 / n  #exterior angle of n sided polygon
    for side in range(n):#draws amount of sides
        t.forward(length)#moves forward
        t.left(angle)#turns left at the angle calculated 

def circle(t, r):#define function to draw circle
    n = 36 
    circumference = 2 * math.pi * r #calculate circumference
    length = circumference / n  #calculate length
    t.penup()
    t.goto(0, -r - 30) 
    t.pendown()

    polygon(t, length, n) 
    
def arc(t,r,angle): #define function to draw arc with extra parameter
  n = 36
  circumference = 2 * math.pi * r #calculate circumference
  length = circumference / n 
  side = int(n*(angle/360))#determine side length based on angle
  angle_draw = 360/n #determines angle
  t.penup()
  t.goto(0, -r ) 
  t.pendown()
  
  for sides in range(side):
    t.forward(length)
    t.left(angle_draw)
bob = turtle.Turtle()
bob.delay = 0.01 #speeds up drawing


draw(bob, 10, 5)#draws tree


bob.penup()
bob.goto(-50, -50) 
bob.pendown()


square(bob, 50)
square(bob, 100)
square(bob, 150)


bob.penup()
bob.goto(100, 100)  
bob.pendown()


polygon(bob, 50, 3)  #draw polygon
polygon(bob, 50, 4)  #draw polygon
polygon(bob, 50, 6)  #draw polygon
polygon(bob, 50, 8)  #draw polygon


bob.penup()
bob.goto(0, -100) 
bob.pendown()


circle(bob, 30) #draw circle
circle(bob, 60) #draw circle
circle(bob, 90)#draw circle

bob.penup()
bob.goto(0,150)
bob.pendown()

arc(bob,50,360)#draws full circle

turtle.done() #call function

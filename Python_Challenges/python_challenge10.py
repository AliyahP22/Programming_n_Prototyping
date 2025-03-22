import turtle
import math 
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

turtle.done() #call function

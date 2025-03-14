#Aliyah Pargan
#Period 1
#03-13-2025 - 03-14-2025
#Python Coding Challenge 7, where we learned how to use the turtle import to draw shapes 
#such as a tree and a square, using code from the turtle import library, functions, and loops

import turtle 
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length*n)
    t.left(angle)
    draw(t, length, n-1)
    t.right(2*angle)
    draw(t, length, n-1)
    t.left(angle)
    t.backward(length*n)
screen=turtle.Screen()    
t=turtle.Turtle()
t.speed(0)
draw(t,10,5)

screen.mainloop()

import turtle

def square(t):
  for sides in range(4):
    t.fd(100)
    t.lt(90)
    
import turtle
bob = turtle.Turtle()
square(bob)
turtle.done()

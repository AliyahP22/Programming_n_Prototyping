#Aliyah Pargan
#Period 1
#03-13-2025 - 03-14-2025
#Python Coding Challenge 7, where we learned how to use the turtle import to draw shapes 
#such as a tree and a square, using code from the turtle import library, functions, and loops

import turtle #import library
def draw(t, length, n): #define function to draw tree
    if n == 0:
        return
    angle = 50
    t.forward(length*n) #cant shortern to fd, as it would cause a error
    t.left(angle) #can't shorten to lt, as it would cause an error
    draw(t, length, n-1)
    t.right(2*angle)
    draw(t, length, n-1)
    t.left(angle)
    t.backward(length*n)
screen=turtle.Screen()    
t=turtle.Turtle()
t.speed(0) #sets speed to fastest
draw(t,10,5) #call function

screen.mainloop() #call function

import turtle #import library 

def square(t):#define function to draw sqaure
  for sides in range(4): #repeats loop only 4 times then stops to draw 4 sides of a sqaure
    t.fd(100)
    t.lt(90)
    
import turtle #import library
bob = turtle.Turtle()
square(bob) #passes the name bob as a argument
turtle.done() #ends code

#Aliyah Pargan
#Period 1
#03-17-2025
#python coding challenge 8

import turtle
#initial code to draw tree
def draw(t,length,n):
  if n  == 0:
    return
  angle = 50
  t.forward(length * n)
  t.left(angle)
  draw(t,length,n-1)
  t.right(2*angle)
  draw(t, length, n-1)
  t.left(angle)
  t.backward(length * n)
  
def square(t):#initial code to draw square
  
  for sides in range(4):#runs loop 4 times for 4 sides
    t.forward(100)
    t.left(90)
bob = turtle.Turtle()

draw(bob,10,6)

bob.penup()#used to avoid overlap
bob.goto(-50,-50)#changes position
bob.pendown()
square(bob)
turtle.done() #call function

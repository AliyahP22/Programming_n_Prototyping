#Aliyah P
#Period 1
#03-18-2025
#Python coding challenge 9: Improving code and drawing polygons
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

def polygon(t,n):#define function to draw polygon with n as a parameter
  angle = 360/n#exterior angle of n sided polygon
  for side in range(n):#draws amount of sides
    t.forward(100)#moves forward
    t.left(angle)#turns left at the angle calculated 
    
bob = turtle.Turtle()
draw(bob,10,6)#draws tree

bob.penup()#used to avoid overlap
bob.goto(-50,-50)#changes position
bob.pendown()

for n in range(5,10): #draws polygons with 5-10 sides
  polygon(bob,n)
  bob.penup()
  bob.forward(150) #moves polygon drawing to a different position
  bob.pendown()
turtle.done() #call function

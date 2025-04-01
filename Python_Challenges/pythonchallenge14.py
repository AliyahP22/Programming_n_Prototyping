#Aliyah P
#03-31-2025
#Period 1
#Python Coding Challenge 14

import turtle# to use its graphics functionality
def draw_spiral(t, n, length, a, b):#function that draws an Archimedean spiral
    """
    Arguments:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosely coiled the spiral is (larger is looser)
    """
    
    theta = 0.0
    for i in range(n):#loop to draw n line segments
        t.forward(length)
        dtheta = 1 / (a + b * theta)#formula to calculate change in angle
        t.left(dtheta)#turns left by calculated angle
        theta += dtheta#updates for next iteration
        length += 0.5
# Create a turtle object named pepito
pepito = turtle.Turtle()

# Create a screen 
screen = turtle.Screen()
# Set the background color red
screen.bgcolor("red")


pepito.color("purple")

# Call the draw_spiral function 
draw_spiral(pepito, 1000, 5, 0.10, 0.1)

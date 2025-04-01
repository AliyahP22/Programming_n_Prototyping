#Aliyah P
#03-28-2025 Period 1
#Python Coding Challenge 13


import turtle #import library needed
def draw_hexagon(t, length): #define function
    vertices = []
    for _ in range(6):
        vertices.append(t.pos())
        t.forward(length)
        t.left(60)
    return vertices#return value
def draw_internal_lines(t, center, vertices):#functions to draw inside lines
    for vertex in vertices:
        t.penup()
        t.goto(center)
        t.pendown()
        t.goto(vertex)
def draw_full_shape(t, length, color):#function to draw shape
    t.color(color)
    t.pendown()
    center = t.pos()
    vertices = draw_hexagon(t, length)
    draw_internal_lines(t, center, vertices)
    t.penup()
def main():#main function
    screen = turtle.Screen()
    screen.bgcolor("pink")#background color
    t = turtle.Turtle()
    t.speed(0)#speed of turtle
    t.width(2)
    colors = ["red", "blue", "green"]#colors of shape
    positions = [(-200, 0), (0, 0), (200, 0)]
    for i, pos in enumerate(positions):
        t.penup()
        t.goto(pos)
        t.pendown()
        draw_full_shape(t, 100, colors[i % len(colors)])
    turtle.done()
main()

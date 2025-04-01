import turtle
def draw_hexagon(t, length):
    vertices = []
    for _ in range(6):
        vertices.append(t.pos())
        t.forward(length)
        t.left(60)
    return vertices
def draw_internal_lines(t, center, vertices):
    for vertex in vertices:
        t.penup()
        t.goto(center)
        t.pendown()
        t.goto(vertex)
def draw_full_shape(t, length, color):
    t.color(color)
    t.pendown()
    center = t.pos()
    vertices = draw_hexagon(t, length)
    draw_internal_lines(t, center, vertices)
    t.penup()
def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    colors = ["red", "blue", "purple"]
    positions = [(-200, 0), (0, 0), (200, 0)]
    for i, pos in enumerate(positions):
        t.penup()
        t.goto(pos)
        t.pendown()
        draw_full_shape(t, 100, colors[i % len(colors)])
    turtle.done()
main()

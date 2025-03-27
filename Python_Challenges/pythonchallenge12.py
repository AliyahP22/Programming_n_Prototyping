#Aliyah P
#Period 1
#03-27-2025
#Python Coding Challenge 12, that draws flowers using functions and loops

import turtle#import library needed
import math#import library needed
def draw_petal(t, r): #define function to draw flower petals
    t.circle(r, 60)  
    t.left(120) #moves the pen tool to the left to draw petal 
    t.circle(r, 60)  
    t.left(120)  #moves the pen tool to the left to draw petal
def draw_flower(t, r, num_petals):#define function to draw flower
    for i in range(num_petals):#repeats a set amount of times
        draw_petal(t, r)  
        t.left(360 / num_petals)  
def main(): #define main function to draw flowers
    bob = turtle.Turtle()
    bob.speed(0)  
    bob.delay = 0.01#speeds up bob
    bob.color("purple") #add color to big flower
    draw_flower(bob, 100, 8) #flower position
    bob.penup()
    bob.goto(0, -50)  
    bob.pendown()
    bob.color("magenta")  #color to little flower
    draw_flower(bob, 50, 8) #flower position 

    turtle.done() #call function

main()#call function

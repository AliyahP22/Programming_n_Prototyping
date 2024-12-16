#Aliyah Pargan
#Periods 1-2
#12-16-2024
# Project stem Assignment: Unit 6
#In this assignment, I would be creating a winter themed animation that includes 5 circles, 5 polygons,5 line commands,
# 2 for loops and 1 global variable

import simplegui
import random

#global variable used for snowfall
snow_fall = []

#values for frame
width = 600
height = 600
snowflakes = 10
snowfall_speed = 1

#code to make snowflakes fall randomly across screen
for i in range(snowflakes):
    snow_fall.append(random.randint(0,height))
    
 
def draw(canvas):
    global snow_fall
    canvas.draw_polygon([(0,0),(width,0),(width,height),(0,height)],1,"white","lightskyblue")
    canvas.draw_line((1, 600), (600, 600), 100, "white")
    canvas.draw_line((1, 500), (600, 500), 100, "white")
    canvas.draw_circle((500, 400), 75, 5, "Snow", "white")
    canvas.draw_circle((500, 290), 60, 5, "Snow", "white")
    canvas.draw_circle((500, 200), 50, 5, "Snow", "white")
    canvas.draw_circle((480, 190), 5, 5, "black", "black")
    canvas.draw_circle((520, 190), 5, 5, "black", "black")
    canvas.draw_polygon([(500, 190), (510, 208), (508, 190)], 3, "darkorange", "darkorange")
    
    
    for i in range(snowflakes):
        snowflake_x = random.randint(0,width)
        snowflake_y = random.randint(0,height)
        canvas.draw_circle((snowflake_x,snow_fall[i]), 3,1,"white", "white")

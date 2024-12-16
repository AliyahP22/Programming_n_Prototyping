#Aliyah Pargan
#Periods 1-2
#12-16-2024
# Project stem Assignment: Unit 6
#In this assignment, I would be creating a winter themed animation that includes 5 circles, 5 polygons,5 line commands,
# 2 for loops and 1 global variable

import simplegui
import random

#message to be displayed
message = "Happy Holidays!!"
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
    canvas.draw_text(message, [170,150],40,"Maroon")
    canvas.draw_line((170, 160), (458, 160), 5, "black")
    canvas.draw_circle((180, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((200, 170),5, 5, "Snow", "green")
    canvas.draw_circle((225, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((245, 170),5, 5, "Snow", "green")
    canvas.draw_circle((265, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((285, 170),5, 5, "Snow", "green")
    canvas.draw_circle((305, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((325, 170),5, 5, "Snow", "green")
    canvas.draw_circle((345, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((365, 170),5, 5, "Snow", "green")
    canvas.draw_circle((385, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((405, 170),5, 5, "Snow", "green")
    canvas.draw_circle((425, 170),5, 5, "Snow", "Red")
    canvas.draw_circle((445, 170),5, 5, "Snow", "green")
    canvas.draw_line((1, 600), (600, 600), 100, "white")
    canvas.draw_line((1, 500), (600, 500), 100, "white")
    canvas.draw_circle((500, 400), 75, 5, "Snow", "white")
    canvas.draw_circle((500, 290), 60, 5, "Snow", "white")
    canvas.draw_circle((500, 200), 50, 5, "Snow", "white")
    canvas.draw_circle((480, 190), 5, 5, "black", "black")
    canvas.draw_circle((520, 190), 5, 5, "black", "black")
    canvas.draw_polygon([(500, 190), (510, 208), (508, 190)], 3, "darkorange", "darkorange")
    canvas.draw_circle((520, 220), 4, 1, "black", "black")
    canvas.draw_circle((500, 220), 4, 1, "black", "black")
    canvas.draw_circle((480, 218), 4, 1, "black", "black")
    canvas.draw_circle((500, 270), 6, 1, "black", "black")
    canvas.draw_circle((500, 290), 6, 1, "black", "black")
    canvas.draw_circle((500, 310), 6, 1, "black", "black")
    
    for i in range(snowflakes):
        snowflake_x = random.randint(0,width)
        snowflake_y = random.randint(0,height)
        canvas.draw_circle((snowflake_x,snow_fall[i]), 3,1,"white", "white")
        
        
        
        
frame = simplegui.create_frame("Project Stem: Winter Animation",width,height)
frame.set_draw_handler(draw)
                  
                  
frame.start()



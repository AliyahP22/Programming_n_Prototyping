#Aliyah Pargan
#Periods 1-2
#12-2-2024
#The Thanksgiving Drawing project is a drawing created by all the functions learned so far, such as drawing polygons
#and drawing circles. I would also be using my own functions to make it fun and interactive! The main goal is to create
#a cute and festive drawing using python


import simplegui

#create frame
frame = simplegui.create_frame("Thanksgiving Drawing", 600,600)
frame.set_canvas_background("black")

message = "Happy Thanksgiving!"
#my function
def click_button():
    global message
    message = "Enjoy the Holiday Season!"
    
# Draw handler function
def draw(canvas):
    #Adding a message to frame
    canvas.draw_text(message, [70,100],40,"Maroon")
    # Example: Drawing a circle
    canvas.draw_circle((300, 200), 50, 5, "Brown", "Orange")
    # Example: Drawing a line
    canvas.draw_line((100, 200), (500, 200), 3, "Black")
    # Example: Drawing a polygon
    canvas.draw_polygon([(250, 250), (350, 250), (300, 300)], 5, "Red", "Yellow")
    # Example: Drawing a point
    canvas.draw_point((300, 200), "Blue")


    # Assign draw handler to the frame
frame.set_draw_handler(draw)
#add button code
frame.add_button("Click here!", click_button)



#start frame
frame.start()
click_button() #call function

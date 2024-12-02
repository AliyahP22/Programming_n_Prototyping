#Aliyah Pargan
#Periods 1-2
#12-2-2024
#The Thanksgiving Drawing project is a drawing created by all the functions learned so far, such as drawing polygons
#and drawing circles. I would also be using my own functions to make it fun and interactive! The main goal is to create
#a cute and festive drawing using python


import simplegui
message = "Happy Thanksgiving!"
#create frame
frame = simplegui.create_frame("Thanksgiving Drawing", 600,600)
frame.set_canvas_background("black")


#my function
def click_button():
    global message
    message = "Enjoy the Holiday Season!"
    
# Draw handler function
def draw_handler(canvas):
    #Adding a message to frame
    canvas.draw_text(message, [70,100],40,"Maroon")
    # Example: Drawing a circle
    canvas.draw_circle((300, 200), 60, 5, "SaddleBrown", "SaddleBrown")
    canvas.draw_circle((313, 200), 5, 5, "black", "black")
    canvas.draw_circle((280, 200), 5, 5, "black", "black")
    canvas.draw_polygon([(320, 210), (285, 210), (312, 227)], 5, "Red", "Yellow")
    canvas.draw_circle((300, 330), 80, 5, "SaddleBrown", "SaddleBrown")
    
  
   
    # Example: Drawing a point
    canvas.draw_point((300, 200), "Blue")


    # Assign draw handler to the frame
frame.set_draw_handler(draw_handler)
#add button code
frame.add_button("Click here!", click_button)



#start frame
frame.start()
click_button() #call function

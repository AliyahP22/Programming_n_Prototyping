#Aliyah Pargan
#Periods 1-2
#12-2-2024
#The Thanksgiving Drawing project is a drawing created by all the functions learned so far, such as drawing polygons
#and drawing circles. I would also be using my own functions to make it fun and interactive! The main goal is to create
#a cute and festive drawing using python


import simplegui
#initial message displayed
message = "Happy Thanksgiving!"
#create frame
frame = simplegui.create_frame("Thanksgiving Drawing", 600,600)
frame.set_canvas_background("chocolate")


#my function
def click_button():
    global message
    message = "Enjoy the Holiday Season!"#displayed after button is clicked
    
# Draw handler function
def draw_handler(canvas):
    #Adding a message to frame
    canvas.draw_text(message, [120,100],40,"Maroon")
    # creating the turkey
    canvas.draw_circle((300, 200), 60, 5, "SaddleBrown", "SaddleBrown")
    canvas.draw_circle((313, 200), 5, 5, "black", "black")
    canvas.draw_circle((280, 200), 5, 5, "black", "black")
    canvas.draw_polygon([(320, 210), (285, 210), (312, 227)], 3, "Red", "Yellow")
    canvas.draw_circle((200, 320), 50, 5, "Gold", "FireBrick")
    canvas.draw_circle((220, 300), 50, 5, "FireBrick", "Gold")
    canvas.draw_circle((370, 345), 50, 5, "FireBrick", "Gold")
    canvas.draw_circle((360, 320), 50, 5, "FireBrick", "Gold")
    canvas.draw_circle((300, 330), 90, 5, "SaddleBrown", "SaddleBrown")
    
   
    #creating the table
    canvas.draw_line((1, 400), (600, 400), 100, "Crimson")
    canvas.draw_line((1, 500), (600, 500), 100, "Crimson")
    canvas.draw_line((1, 600), (600, 600), 100, "Crimson")
  
   # drawing the plates for table 
    canvas.draw_circle((35, 400), 30, 5, "Black", "Slategray")
    canvas.draw_circle((35, 400), 20, 4, "Black", "Slategray")
    canvas.draw_circle((300, 400),30, 5, "Black", "Slategray")
    canvas.draw_circle((300, 400), 20, 4, "Black", "Slategray")
    canvas.draw_circle((500, 400),30, 5, "Black", "Slategray")
    canvas.draw_circle((500, 400), 20, 4, "Black", "Slategray")
    canvas.draw_circle((300, 570),30, 5, "Black", "Slategray")
    canvas.draw_circle((300, 570), 20, 4, "Black", "Slategray")
    canvas.draw_circle((35, 570), 30, 5, "Black", "Slategray")
    canvas.draw_circle((35, 570), 20, 4, "Black", "Slategray")
    canvas.draw_circle((500, 570), 30, 5, "Black", "Slategray")
    canvas.draw_circle((500, 570), 20, 4, "Black", "Slategray")
    
    
    # Example: Drawing a point
    canvas.draw_point((300, 200), "Blue")


    # Assign draw handler to the frame
frame.set_draw_handler(draw_handler)
#add button code
frame.add_button("Click here!", click_button) #calls function



#start frame
frame.start()



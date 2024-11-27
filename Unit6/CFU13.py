#Aliyah Pargan
#Period 2
#11-26-2024
#In CFU 13, using the canvas we have created, we are going to create a smiley face
#using dots and coordinates 


import simplegui 

def draw_handler(canvas):
    # Left Eye
    canvas.draw_point([50, 70], "blue")
    canvas.draw_point([50, 72], "blue")

    
    # Right Eye
    canvas.draw_point([140, 70], "blue")
    canvas.draw_point([140, 72], "blue")

    
    # Smile
    canvas.draw_point([70, 130], "red")
    canvas.draw_point([72, 132], "red")
    canvas.draw_point([74, 134], "red")
    canvas.draw_point([76, 135], "red")
    canvas.draw_point([78, 136], "red")
    canvas.draw_point([80, 137], "red")
    canvas.draw_point([82, 137], "red")
    canvas.draw_point([84, 137], "red")
    canvas.draw_point([86, 136], "red")
    canvas.draw_point([88, 135], "red")
    canvas.draw_point([90, 134], "red")
    canvas.draw_point([92, 132], "red")
    canvas.draw_point([94, 130], "red")
    
# Create frame
frame = simplegui.create_frame("CFU13 Happy Dots", 200, 200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)

# Start frame
frame.start()

#Aliyah Pargan
#Period 2
#11-26-2024
#In CFU 14, using the canvas we have created, we are going to create a smiley face using the canvas draw_line method and using this method,
#I would adjust the line width and height.
import simplegui 

def draw_handler(canvas):
    # Left Eye
    canvas.draw_line([70,100],[75,102], 5,"blue")
   
    
    # Right Eye
    canvas.draw_line([90,100],[95,102], 5,"blue")


    
    # Smile
    canvas.draw_line([70, 130],[72, 132],5,"blue")
    canvas.draw_line([74, 134],[76, 135], 5,"blue")
    canvas.draw_line([78, 136],[80, 137], 5,"blue")
    canvas.draw_line([82, 137],[84, 137], 5,"blue")
    canvas.draw_line([86, 136],[88, 135], 5,"blue")
    canvas.draw_line([90, 134],[92, 132], 5,"blue")
    
    
# Create frame
frame = simplegui.create_frame("CFU14 Happy Lines", 200, 200)
frame.set_canvas_background("pink")
frame.set_draw_handler(draw_handler)

# Start frame
frame.start()

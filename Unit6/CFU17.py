#Aliyah Pargan
#Period 2
#12-6-2024
#CFU 17, where we use functions to draw texts and images

import simplegui
message = "Hello World!!"
color1 = input("Enter a color!")
frame_width = int(input("Initial Width?"))
frame_height = int(input("Initial Height?"))

def draw(canvas):
    canvas.draw_line([0,0],[100,100],3,color1)
    canvas.draw_text(message,[frame_width/2,frame_height/2],30,color1)
    




#frame = simplegui.create_frame("CFU17", 300,200)
frame = simplegui.create_frame("CFU17",frame_width,frame_height)
frame.set_canvas_background("lavenderblush")
frame.set_draw_handler(draw)
frame.start()

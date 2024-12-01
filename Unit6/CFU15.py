#Aliyah Pargan
#Period 1-2
#11-27-2024
#CFU 15, which is a practice of how to use the canvas.draw_polygon function to create
#a happy face on a 200 by 200 frame, using simplegui.


import simplegui


def draw_handler(canvas):
    #left eye
   canvas.draw_polygon([(30,45),(30,75),(70,45)], 5, "black")
    #right eye
   canvas.draw_polygon([(110,45),(110,75),(135,45)], 5, "black")
    #smile
   canvas.draw_polygon([(60,115),(90,140),(130,115)], 5, "black")
   

#Creates frame
frame = simplegui.create_frame("CFU15 Happy Shapes",200,200)
frame.set_canvas_background("lavenderblush")
frame.set_draw_handler(draw_handler)


#start frame
frame.start()

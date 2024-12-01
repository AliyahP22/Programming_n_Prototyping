import simplegui


def draw_handler(canvas):
    #left eye
   canvas.draw_polygon([(70,100),(75,102),(80,105)], 5, "black")
   




#Creates frame
frame = simplegui.create_frame("CFU15 Happy Shapes",200,200)
frame.set_canvas_background("pink")
frame.set_draw_handler(draw_handler)


#start frame
frame.start()

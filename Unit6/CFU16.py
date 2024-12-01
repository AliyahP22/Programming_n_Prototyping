#Aliyah Pargan
#Periods 1-2
#12-1-2024
#CFU 16, which is a practice of using the canvas.draw_circle to create a happy face on a
#200 by 200 frame using simplegui

import simplegui








#create frame
frame = simplegui.create_frame("CFU 16 Happy Circles", 200,200)
frame.set_canvas_background("lavenderblush")
frame.set_draw_handler(draw_handler)

#start frame
frame.start()



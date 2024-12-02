#Aliyah Pargan
#Periods 1-2
#12-1-2024
#CFU 16, which is a practice of using the canvas.draw_circle to create a happy face on a
#200 by 200 frame using simplegui

import simplegui
def draw_handler(canvas):
    canvas.draw_circle((100, 100), 60, 5, "Black", "Mediumvioletred")
    canvas.draw_circle((75, 80), 5, 5, "Black", "black")
    canvas.draw_circle((112, 80), 5, 5, "Black", "black")
    canvas.draw_circle((70, 120), 3, 5, "Black", "black")
    canvas.draw_circle((70, 120), 3, 5, "Black", "black")
    canvas.draw_circle((70, 120), 3, 5, "Black", "black")






#create frame
frame = simplegui.create_frame("CFU 16 Happy Circles", 200,200)
frame.set_canvas_background("lavenderblush")
frame.set_draw_handler(draw_handler)

#start frame
frame.start()



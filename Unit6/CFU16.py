##Aliyah Pargan
#Periods 1-2
#12-1-2024
#CFU 16, which is a practice of using the canvas.draw_circle to create a happy face on a
#200 by 200 frame using simplegui

import simplegui
def draw_handler(canvas):
    canvas.draw_circle((100, 100), 60, 5, "Black", "Mediumvioletred")
    canvas.draw_circle((75, 80), 5, 5, "Black", "black")
    canvas.draw_circle((112, 80), 5, 5, "Black", "black")
    canvas.draw_circle((70, 130), 3, 5, "Black", "black")
    canvas.draw_circle((72, 132), 3, 5, "Black", "black")
    canvas.draw_circle((74, 134), 3, 5, "Black", "black")
    canvas.draw_circle((76, 136), 3, 5, "Black", "black")
    canvas.draw_circle((78, 138), 3, 5, "Black", "black")







#create frame
frame = simplegui.create_frame("CFU 16 Happy Circles", 200,200)
frame.set_canvas_background("lavenderblush")
frame.set_draw_handler(draw_handler)

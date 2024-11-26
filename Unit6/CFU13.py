#Aliyah Pargan
#Period 2
#11-26-2024
#In CFU 13, using the canvas we have created, we are going to create a smiley face
#using dots and coordinates 



import simplegui

def draw_handler(canvas):
    #create the drawing
    #canvas.draw_point([x,y],"color")
    
    canvas.draw_point([100,109],"red")
    canvas.draw_point([100,100],"red")
    canvas.draw_point([107,100],"red")
    canvas.draw_point([111,107],"red")
    canvas.draw_point([109,107],"red")
    canvas.draw_point([108,107],"red")
    canvas.draw_point([107,107],"red")
    canvas.draw_point([106,107],"red")
    canvas.draw_point([105,108],"red")
    canvas.draw_point([104,108],"red")
    canvas.draw_point([103,108],"red")
    canvas.draw_point([102,108],"red")
    canvas.draw_point([101,108],"red")
    canvas.draw_point([100,108],"red")
    canvas.draw_point([99,108],"red")
    canvas.draw_point([98,108],"red")
    canvas.draw_point([97,108],"red")
    canvas.draw_point([96,108],"red")
    canvas.draw_point([95,108],"red")
    canvas.draw_point([94,107],"red")
    canvas.draw_point([93,107],"red")
    canvas.draw_point([92,106],"red")
frame= simplegui.create_frame("CFU 13: Happy Face", 200,200)
frame.set_canvas_background("cyan")
frame.set_draw_handler(draw_handler)
frame.start()

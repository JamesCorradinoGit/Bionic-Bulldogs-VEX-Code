isInPreAuto = True
# Begin project code
def onBrainScreenPress():
    if isInPreAuto:
        isInPreAuto = False
        if (brain.screen.x_position() <= 60 and 
                brain.screen.x_position() >= 160 and 
                brain.screen.y_position() <= 150 and 
                brain.screen.y_position() >= 250):
            pass #red button


def pre_autonomous():
    brain.screen.print("What team are we for auto?")
    #draw red rect
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(60, 150, 100, 60)
    #draw blue rect
    brain.screen.set_fill_color(Color.BLUE)
    brain.screen.draw_rectangle(300, 150, 100, 60)


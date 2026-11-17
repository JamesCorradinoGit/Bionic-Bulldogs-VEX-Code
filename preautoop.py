isInPreAuto = True
isOnRedTeam = False
isOnBlueTeam = False
# Begin project code
def onBrainScreenPress():
    global isInPreAuto
    if (isInPreAuto == True):
        if (brain.screen.x_position() <= 60 and 
                brain.screen.x_position() >= 160 and 
                brain.screen.y_position() <= 150 and 
                brain.screen.y_position() >= 250):
            isInPreAuto = False
            isOnRedTeam = True
            brain.screen.clear_screen()
        elif (brain.screen.x_position() <= 300 and 
                brain.screen.x_position() >= 400 and 
                brain.screen.y_position() <= 150 and 
                brain.screen.y_position() >= 250):
            isInPreAuto = False
            isOnBlueTeam = True
            brain.screen.clear_screen()
            brain.screen.print("blue")

def pre_autonomous():
    brain.screen.pressed(onBrainScreenPress)
    brain.screen.print("What team are we for auto?")
    #draw red rect
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(60, 150, 100, 60)
    #draw blue rect
    brain.screen.set_fill_color(Color.BLUE)
    brain.screen.draw_rectangle(300, 150, 100, 60)


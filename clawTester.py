# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  drivetrain on motors 1234 and motor on 5
# 
# ------------------------------------------

# Library imports
from vex import *
import time

#max angle is x and min angle is y

# Begin project code
while True:
    brain.screen.clear_screen()
    if controller_1.buttonR1.pressing():
        motor_5.spin(FORWARD)
    if controller_1.buttonR2.pressing():
        motor_5.spin(REVERSE)
    else:
        motor_5.stop()
    brain.screen.set_cursor(1, 1)
    brain.screen.print(motor_5.position(DEGREES))
    wait(1,SECONDS)

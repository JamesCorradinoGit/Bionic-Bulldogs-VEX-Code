clawOpen:bool = False
motor_19.set_stopping(HOLD)
motor_19.set_velocity(5, PERCENT)

motor_19.set_position(0, DEGREES)
while True:
   # motor_19.set_timeout(0.3, SECONDS)
    if controller_1.buttonUp.pressing() and motor_19.is_spinning() == False and clawOpen == False:
        motor_19.spin_to_position(10, DEGREES)
        clawOpen = True

    elif controller_1.buttonDown.pressing() and motor_19.is_spinning() == False and clawOpen == True:
        motor_19.spin_to_position(-10, DEGREES)
        clawOpen = False
    wait(30, MSEC)

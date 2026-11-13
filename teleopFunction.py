motor_19.set_stopping(HOLD)
motor_19.set_velocity(5, PERCENT)

motor_19.set_position(0, DEGREES)
while True:
    if controller_1.buttonUp.pressing():
        if motor_19.position(DEGREES)>= 10 and motor_19.position(DEGREES)<=45:
            motor_19.spin_for(FORWARD, 2, DEGREES)
            controller_1.rumble("-..-..-")
            motor_19.set_timeout(10, MSEC)
        
    if controller_1.buttonDown.pressing():    
        if motor_19.position(DEGREES) <=45 and motor_19.position(DEGREES)>=10:
            motor_19.spin_for(REVERSE, 2, DEGREES)
            controller_1.rumble(".--.--.")
            motor_19.set_timeout(10, MSEC)
    wait(30, MSEC)

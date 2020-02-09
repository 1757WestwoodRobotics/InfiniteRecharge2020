# Westwood FRC Team 1757
# 2020

# A central place to activate all subsystems required by the robot.
#
# OK, so what do I do?
#
# (1) 'import' your Subsystem type
# (2) declare an instance of your Subsystem type and set it to None
# (3) In the init() function:
#        - declare your instance as 'global'
#        - instantiate your instance by call its constructor
#     (The init() function is called from our robotInit() function)
#
# P.S. There's probably a better way to do this than rely on 'global' (yuck)
#      but we can always revisit this later.

import subsystems.colorsensor
import subsystems.singlemotor


revColorSensor = None
singleMotor = None

def init():
    global revColorSensor
    global singleMotor

    revColorSensor = subsystems.colorsensor.ColorSensorSubsystem()
    singleMotor = subsystems.singlemotor.SingleMotor()

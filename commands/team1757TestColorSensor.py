# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the REV Robotics ColorSensorV3
#
# ATTENTION!!!!
# THIS IS *TEST* CODE!  DO *NOT* DO DEVELOPMENT IN THIS FILE!
# IT SHOULD ONLY BE USED FOR BASIC SANITY CHECKS ON THE COLOR SENSOR ITSELF,
# PLUS WE WILL NEED IT TO CALIBRATE CONTROL PANEL REFERENCE COLORS ON 
# COMPETITION DAY.
#
# Thank you.


import wpilib
from wpilib.command import Command
import subsystems

class Team1757TestColorSensorCommand(Command):

    def __init__(self):
        Command.__init__(self)

        self.requires(subsystems.team1757Subsystems.gREVColorSensor)
        

    def execute(self):
        theSensor = subsystems.team1757Subsystems.gREVColorSensor
        # Get the sensor attributes
        color = theSensor.color
        ir = theSensor.ir

        # Get the individual components of the color
        red = color.red
        blue = color.blue
        green = color.green

        # Get the approximate proximity of an object
        proximity = theSensor.proximity

        print("Color: {}, IR: {}, Red: {}, Blue: {}, Green: {}, Prox: {}".format(color, ir, red, blue, green, proximity))

    def isFinished(self):
        return False

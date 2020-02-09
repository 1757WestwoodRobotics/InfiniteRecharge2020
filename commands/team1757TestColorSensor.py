# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the REV Robotics ColorSensorV3

import wpilib
from wpilib.command import Command
from subsystems import team1757Subsystems

class Team1757TestColorSensorCommand(Command):

    def __init__(self):
        Command.__init__(self)

        self.requires(team1757Subsystems.revColorSensor)
        
    # This just repeatedly samples the color sensor and prints out the results.
    def execute(self):
        theSensor = team1757Subsystems.revColorSensor
        # Get the sensor attributes
        color = theSensor.color
        ir = theSensor.ir

        # Get the individual components of the color
        red = theSensor.red
        blue = theSensor.blue
        green = theSensor.green

        # Get the approximate proximity of an object
        proximity = theSensor.proximity

        print("IR: {}, Red: {}, Blue: {}, Green: {}, Prox: {}".format(ir, red, blue, green, proximity))

    def isFinished(self):
        return False
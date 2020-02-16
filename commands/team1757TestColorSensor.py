# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the REV Robotics ColorSensorV3

import wpilib
from wpilib.command import Command
import subsystems

class Team1757TestColorSensorCommand(Command):

    def __init__(self):
        Command.__init__(self)
        print("Team1757TestColorSensorCommand init called")

        self.requires(subsystems.team1757Subsystems.gREVColorSensor)
        

    def execute(self):
        print("Team1757TestColorSensorCommand execute called")
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
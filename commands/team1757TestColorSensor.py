# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the REV Robotics ColorSensorV3

from wpilib.command import Command


class Team1757TestColorSensorCommand(Command):

    def __init__(self):
        self.requires(subsystems.team1757Subsystems.revColorSensor)

    def execute(self):
        theSensor = subsystems.team1757Subsystems.revColorSensor
        # Get the sensor attributes
        color = theSensor.color
        ir = theSensor.ir

        # Get the individual components of the color
        red = theSensor.red
        blue = theSensor.blue
        green = theSensor.green

        # Get the approximate proximity of an object
        proximity = theSensor.proximity

        print("Color: {0}, IR: {1}, Red: {2}, Blue: {3}, Green: {4}, Prox: {5}", color, ir, red, blue, green, proximity)
# Westwood FRC Team 1757
# 2020

# Color sensor subsystem wrapper around the REV Robotics ColorSensorV3 sensor.

from rev.color import ColorSensorV3
from wpilib.command import Subsystem


class ColorSensorSubsystem(Subsystem):
    def __init__(self):
        Subsystem.__init__(name=ColorSensorSubsystem)
        
        self.__colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    @property
    def color(self):
        return self.__colorSensor.getColor()

    @property
    def ir(self):
        return self.__colorSensor.getIR()

    @property
    def red(self):
        return self.__colorSensor.red

    @property
    def green(self):
        return self.__colorSensor.green

    @property
    def blue(self):
        return self.__colorSensor.blue

    @property
    def proximity(self):
        return self.__colorSensor.getProximity()


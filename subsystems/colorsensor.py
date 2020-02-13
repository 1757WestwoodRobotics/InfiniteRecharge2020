# Westwood FRC Team 1757
# 2020

# Color sensor subsystem wrapper around the REV Robotics ColorSensorV3 sensor.
import wpilib
from rev.color import ColorSensorV3
from wpilib.command import Subsystem


class ColorSensorSubsystem(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, name="ColorSensorSubsystem")
        
        self.__colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    @property
    def color(self):
        return self.__colorSensor.getColor()

    @property
    def ir(self):
        return self.__colorSensor.getIR()

    @property
    def red(self):
        return self.color.red

    @property
    def green(self):
        return self.color.green

    @property
    def blue(self):
        return self.color.blue

    @property
    def proximity(self):
        return self.__colorSensor.getProximity()


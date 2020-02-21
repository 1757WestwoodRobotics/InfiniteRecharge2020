# Westwood FRC Team 1757
# 2020

# Control panel subsystem, incorporating a REV Robotics ColorSensorV3 sensor
# and WPI_TalonSRX motor to rotate colored control panel disk to desired color.

import wpilib
from wpilib.command import Subsystem
from rev.color import ColorSensorV3
from ctre import WPI_TalonSRX, ControlMode

# Team 1757 stuff
from robotmap import Can
from robotmap import ColorPanelConst


class ControlPanel(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, name="ControlPanel")
        
        self.__colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.__motor = WPI_TalonSRX(Can.controlPanel)
        self.__targetColor = ColorPanelConst.PanelColors.Red

    def setTargetColor(self, targetColor):
        self.__targetColor = targetColor

    # Not really needed for API, but might be handy for testing?
    @property
    def sensorColor(self):
        return self.__colorSensor.getColor()

    # Kind of simplistic for now ...
    @property
    def currentPanelColor(self):
        sensorRGB = self.sensorColor
        if (sensorRGB.blue > ColorPanelConst.Threshold):
            return ColorPanelConst.PanelColors.Blue
        elif (sensorRGB.red > ColorPanelConst.Threshold):
            if (sensorRGB.green > ColorPanelConst.Threshold):
                return ColorPanelConst.PanelColors.Yellow
            else:
                return ColorPanelConst.PanelColors.Red
        else:
            return ColorPanelConst.PanelColors.Green

    def getBestDirection(self):
        currentColor = self.currentPanelColor
        return -1 if self.__targetColor - currentColor == -1 else 1

    @property
    def found(self):
        return self.currentPanelColor == self.__targetColor


    def seek(self):
        
        if (self.found()):
            return

        bestDirection = self.getBestDirection()

        speed = 0.1  # Here temporarily.  Should be in a central location
        self.__motor.set(ColorPanelConst.RotationSense*bestDirection*speed)



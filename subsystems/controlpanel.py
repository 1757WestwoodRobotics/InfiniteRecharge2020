# Westwood FRC Team 1757
# 2020

# Control panel subsystem, incorporating a REV Robotics ColorSensorV3 sensor
# and WPI_TalonSRX motor to rotate colored control panel disk to desired color.

import wpilib
from wpilib import Solenoid
from wpilib.command import Subsystem
from rev.color import ColorSensorV3
from ctre import WPI_TalonSRX, ControlMode

# Team 1757 stuff
from robotmap import Can
from robotmap import ColorPanelConst
from robotmap import PCM
from libs1757.vector import Vector
from commands.testControlPanelColor import TestControlPanelColor



class ControlPanel(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, name="ControlPanel")

        self.controlPanel = Solenoid(Can.PCM, PCM.ControlPanel)
        
        # hardware we are using
        self.__colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.__motor = WPI_TalonSRX(Can.controlPanel)

        # handy working variables ---------------------------------------------------------------

        # The "official" panel color that we are reporting
        self.__cachedPanelColor = ColorPanelConst.PanelColors.Reset

        # Working parameters used to determine "official" reported panel color
        self.__previousColor = ColorPanelConst.PanelColors.Reset
        self.__colorCount = 0
        self.__GreenYellowDiff = (ColorPanelConst.ReferenceGreen - ColorPanelConst.ReferenceYellow).magnitude()**2

        # default target color to seek
        self.__targetColor = ColorPanelConst.PanelColors.Red


    def setTargetColor(self, targetColor):
        self.__targetColor = targetColor


    # Not really needed for API, but might be handy for testing?
    @property
    def sensorColor(self):
        return self.__colorSensor.getColor()


    # Gets the current official color, *without* doing an update
    @property
    def currentPanelColor(self):
        return self.__cachedPanelColor


    def currentColorIsValid(self):
        return self.currentPanelColor != ColorPanelConst.PanelColors.Junk and \
               self.currentPanelColor != ColorPanelConst.PanelColors.Reset


    # Incorporates Sam's research.  Updates our internally cached current color.
    def updatePanelColor(self):
        sensorRGB = self.sensorColor
        sensorColorVec = Vector(sensorRGB.red, sensorRGB.green, sensorRGB.blue)

        redDist = (sensorColorVec - ColorPanelConst.ReferenceRed).magnitude()
        currentColor = ColorPanelConst.PanelColors.Red
        minDist = redDist

        greenDist = (sensorColorVec - ColorPanelConst.ReferenceGreen).magnitude()
        if (greenDist < minDist):
            currentColor = ColorPanelConst.PanelColors.Green
            minDist = greenDist

        blueDist = (sensorColorVec - ColorPanelConst.ReferenceBlue).magnitude()
        if (blueDist < minDist):
            currentColor = ColorPanelConst.PanelColors.Blue
            minDist = blueDist

        yellowDist = (sensorColorVec - ColorPanelConst.ReferenceYellow).magnitude()
        if (yellowDist < minDist):
            currentColor = ColorPanelConst.PanelColors.Yellow
            minDist = blueDist

        if (minDist**2 >= 0.03*self.__GreenYellowDiff):
            currentColor = ColorPanelConst.PanelColors.Junk

        if (currentColor == self.__previousColor):
            self.__colorCount += 1
        else:
            self.__colorCount = 0

        self.__previousColor = currentColor

        threshold = 3
        if (currentColor == ColorPanelConst.PanelColors.Junk):
            threshold = 10

        if (self.__colorCount >= threshold and currentColor != self.currentPanelColor):
            self.currentPanelColor = currentColor


    def getBestDirection(self):
        currentColor = self.currentPanelColor
        return -1 if self.__targetColor - currentColor == -1 else 1


    @property
    def found(self):
        return self.currentPanelColor == self.__targetColor


    def seek(self):
        
        self.updatePanelColor()

        if (self.found() or not self.currentColorIsValid()):
            self.__motor.set(0.0)
            return
        else:
            bestDirection = self.getBestDirection()
            
            speed = 0.1  # Here temporarily.  Should be in a central location
            self.__motor.set(ColorPanelConst.RotationSense*bestDirection*speed)


    def initDefaultCommand(self):
        self.setDefaultCommand(TestControlPanelColor())
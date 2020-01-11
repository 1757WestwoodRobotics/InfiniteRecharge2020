import wpilib
from wpilib import drive
from ctre import TalonSRX

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        talon1 = TalonSRX(5)
        talon2 = TalonSRX(9)
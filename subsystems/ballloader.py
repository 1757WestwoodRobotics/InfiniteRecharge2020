import wpilib
from ctre import WPI_TalonSRX
from robotmap import Can
from wpilib.command import Subsystem

class BallLoader(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Ball Loader")

        self.upper = WPI_TalonSRX(Can.ballLoader2)
        self.lower = WPI_TalonSRX(Can.ballLoader1)

    def spin(self, lowerSpeed, upperSpeed):
        self.upper.set(upperSpeed)
        self.lower.set(lowerSpeed)

    def stopSpin(self):
        self.upper.set(0)
        self.lower.set(0)
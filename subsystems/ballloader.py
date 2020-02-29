import wpilib
from wpilib import Solenoid
from ctre import WPI_TalonSRX
from robotmap import Can, PCM
from wpilib.command import Subsystem

class BallLoader(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Ball Loader")

        self.indexer = Solenoid(Can.PCM, PCM.Indexer)
        self.upper = WPI_TalonSRX(Can.ballShooterUpper)
        self.lower = WPI_TalonSRX(Can.ballShooterLower)

    def spin(self, speed):
        self.upper.set(speed)
        self.lower.set(speed)

    def stopSpin(self):
        self.upper.set(0)
        self.lower.set(0)
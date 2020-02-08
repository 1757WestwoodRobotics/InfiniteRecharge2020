import wpilib
from ctre import WPI_TalonSRX
from robot import *
from wpilib.command.subsystem import Subsystem

class Ballshooter(Subsystem):

    def __init__(self):
        Subsystem.__init__(name=Ballshooter)
        
        self.ballTalon1 = WPI_TalonSRX(Can.BallShooter1)
        self.ballTalon2 = WPI_TalonSRX(Can.BallShooter2])
import wpilib
from ctre import WPI_TalonSRX
from robot import *
from wpilib.command.subsystem import Subsystem

class Ballshooter(Subsystem):

    def init(self):
        self.ballTalon1 = WPI_TalonSRX(can["ballshooter1"])
        self.ballTalon2 = WPI_TalonSRX(can["ballshooter2"])
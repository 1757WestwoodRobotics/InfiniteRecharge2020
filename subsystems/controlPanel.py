import wpilib
from ctre import WPI_TalonSRX
from robot import *
from wpilib.command.subsystem import Subsystem

class ControlPanel(Subsystem):

    def init(self):
        self.CPTalon = WPI_TalonSRX(can["controlPanel"])
        self.CPTalon.setNeutralMode(neutralModes["brake"])
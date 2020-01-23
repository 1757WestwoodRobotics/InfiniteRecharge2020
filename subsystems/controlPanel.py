import wpilib
from ctre import WPI_TalonSRX
from robot import *
from wpilib.command.subsystem import Subsystem

class ControlPanel(Subsystem):

    def __init__(self):
        super().__init__(name=ControlPanel)

        self.CPTalon = WPI_TalonSRX(can["controlPanel"])
        self.CPTalon.setNeutralMode(neutralModes["brake"])

    def ControlPanelSpin(self, descolor):
        if descolor == self.color:
            self.CPTalon.set(0)
        else:
            self.CPTalon.set(1)
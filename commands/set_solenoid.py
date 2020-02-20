import wpilib
from wpilib import SmartDashboard
from wpilib.command import InstantCommand
import subsystems

class SetSolenoid(InstantCommand):

    def __init__(self, solenoid, position):
        InstantCommand.__init__(self, "Set Solenoid")

        self.requires(subsystems.team1757Subsystems.pneumatics)
        
        self.solenoid = solenoid
        self.position = position

    def initialize(self):
        subsystems.team1757Subsystems.pneumatics.setSolenoid(self.solenoid, self.position)

    def isFinished(self):
        return False
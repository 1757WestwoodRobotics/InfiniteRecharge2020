import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class Compress(Command):

    def __init__(self):
        Command.__init__(self, "Compress")

        self.requires(subsystems.team1757Subsystems.pneumatics)

    def execute(self):
        subsystems.team1757Subsystems.pneumatics.setCompressor(True)

    def isFinished(self):
        return False
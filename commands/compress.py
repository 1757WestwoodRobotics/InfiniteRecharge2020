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
        print("Compressing")
        subsystems.team1757Subsystems.pneumatics.setCompressor(True)

    def end(self):
        subsystems.team1757Subsystems.pneumatics.setCompressor(False)

    def isFinished(self):
        return False
import wpilib
from wpilib.command import Command
import subsystems

class SetDriveLimit(Command):
    '''
    Command to set a software limit of the drivetrain
    '''

    def __init__(self, percentLimit):
        Command.__init__(self, "Set Drive Limit")

        self.limit = percentLimit

    def initialize(self):
        subsystems.team1757Subsystems.drivetrain.coefficient = self.limit

    def end(self):
        subsystems.team1757Subsystems.drivetrain.coefficient = 1

    def isFinished(self):
        return False 
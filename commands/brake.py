import wpilib
from wpilib.command import Command
import subsystems

class Brake(Command):
    '''
    Command to set the drive motors to brake mode

    When the command initializes, brake mode is activated; when the command ends, brake mode ends
    '''

    def __init__(self):
        Command.__init__(self, "Brake")

    def initialize(self):
        print("Init")
        subsystems.team1757Subsystems.drivetrain.setNeutralMode(True)

    def end(self):
        print("End")
        subsystems.team1757Subsystems.drivetrain.setNeutralMode(False)

    def isFinished(self):
        return False 
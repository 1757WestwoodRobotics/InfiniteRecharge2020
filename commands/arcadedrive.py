import wpilib
from wpilib.command import Command
import subsystems

class ArcadeDrive(Command):
    '''
    Command to drive robot using xbox controller arcade drive

    Parameters:

    Squared Inputs: If arcade drive should scale inputs exponentially to create more gradual acceleration; if not specified, defaults False
    '''

    def __init__(self, SquaredInputs = True):
        Command.__init__(self, "ArcadeDrive")

        self.requires(subsystems.team1757Subsystems.drivetrain)

        self.squaredInputs = SquaredInputs

    def execute(self):
        self.speed = -self.getRobot().oi.xboxController.getRawAxis(1)
        self.rotation = self.getRobot().oi.xboxController.getRawAxis(4)

        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.speed, self.rotation, self.squaredInputs)

    def isFinished(self):
        return False
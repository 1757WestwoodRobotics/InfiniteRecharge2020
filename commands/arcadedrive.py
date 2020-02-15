import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class ArcadeDrive(Command):

    def __init__(self):
        Command.__init__(self, "ArcadeDrive")

        self.requires(subsystems.team1757Subsystems.drivetrain)

    def execute(self):
        self.speed = -self.getRobot().oi.xboxController.getRawAxis(1)
        self.rotation = self.getRobot().oi.xboxController.getRawAxis(4)

        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.speed, self.rotation)

    def isFinished(self):
        return False
import wpilib
from wpilib import SmartDashboard
from ctre import WPI_TalonSRX
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class ArcadeDrive(Command):

    def __init__(self, SquaredInputs = True):
        Command.__init__(self, "ArcadeDrive")

        self.requires(subsystems.team1757Subsystems.drivetrain)

        self.squaredInputs = SquaredInputs

        self.testmotor = WPI_TalonSRX(1)

    def execute(self):
        self.speed = -self.getRobot().oi.xboxController.getRawAxis(1)
        self.rotation = self.getRobot().oi.xboxController.getRawAxis(4)

        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.speed, self.rotation, self.squaredInputs)

    def isFinished(self):
        return False
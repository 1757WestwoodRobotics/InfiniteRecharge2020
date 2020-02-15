import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class TankDrive(Command):

    def __init__(self):
        Command.__init__(self, "TankDrive")

        self.requires(subsystems.team1757Subsystems.drivetrain)

    def execute(self):
        self.leftSpeed = -self.getRobot().oi.xboxController.getRawAxis(1)
        self.rightSpeed = -self.getRobot().oi.xboxController.getRawAxis(5)

        subsystems.team1757Subsystems.drivetrain.tankDrive(self.leftSpeed, self.rightSpeed)

    def isFinished(self):
        return False
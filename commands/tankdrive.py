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
        self.leftSpeed = -self.getRobot().oi.leftStick.getY()
        self.rightSpeed = -self.getRobot().oi.rightStick.getY()

        subsystems.team1757Subsystems.drivetrain.tankDrive(self.leftSpeed, self.rightSpeed, True)

    def isFinished(self):
        return False
import wpilib
from wpilib.command import Command
from subsystems.drivetrain import Drivetrain

class Drive(Command):

    def __init__(self):
        Command.__init__(name=Drive, subsystem=Drivetrain)

        self.requires(self.getRobot().drivetrain)

    def execute(self):
        self.speed = self.getRobot().oi.xboxController.getY()

        self.getRobot().drivetrain.arcadeDrive()
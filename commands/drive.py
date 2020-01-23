import wpilib
from wpilib.command import Command
from subsystems.drivetrain import Drivetrain

class Drive(Command):

    def __init__(self):
        super().__init__(name=Drive, subsystem=Drivetrain)

    def execute(self):
        return super().execute()
        
        Drivetrain.differentialDrive.arcadeDrive()
import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class DriveForward(Command):

    def __init__(self, timeout = 0, output = 1):
        Command.__init__(self, "DriveForward")

        self.requires(subsystems.team1757Subsystems.drivetrain)
        self.timer = wpilib.Timer()
        self.timer.start()
        self.timeout = timeout
        self.output = output

    def execute(self):

        self.time = self.timer.get()
        
        if self.time <= self.timeout:
            subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.output, 0)

    def isFinished(self):
        return False
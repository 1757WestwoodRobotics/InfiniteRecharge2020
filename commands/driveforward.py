import wpilib
from wpilib import SmartDashboard
from wpilib.command import TimedCommand
from wpilib.interfaces import GenericHID
import subsystems

class DriveForward(TimedCommand):

    def __init__(self, timeout = 0, output = 1):
        TimedCommand.__init__(self, "DriveForward", timeout)

        self.requires(subsystems.team1757Subsystems.drivetrain)

    def execute(self):
        
        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.output, 0)

    def isFinished(self):
        return False
import wpilib
from wpilib import SmartDashboard
from wpilib.command import TimedCommand
from wpilib.interfaces import GenericHID
import subsystems

class DriveForward(TimedCommand):

    def __init__(self, timeout = 0, output = 1):
        TimedCommand.__init__(self, "DriveForward", timeout=timeout)

        self.requires(subsystems.team1757Subsystems.drivetrain)
        self.output = output

    def execute(self):
        
        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.output, 0, False)
   
    def end(self):

        subsystems.team1757Subsystems.drivetrain.arcadeDrive(0, 0, False)

    def isFinished(self):
        return False
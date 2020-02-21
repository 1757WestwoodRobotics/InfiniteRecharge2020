import wpilib
from wpilib import SmartDashboard
from wpilib.command import TimedCommand
from wpilib.interfaces import GenericHID
import subsystems

class DriveForward(TimedCommand):

    def __init__(self, output = 1, timeout = 0):
        TimedCommand.__init__(self, "Drive Forward", timeout)
        self.requires(subsystems.team1757Subsystems.drivetrain)

        self.output = output

    def execute(self):
        
        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.output, 0, False)
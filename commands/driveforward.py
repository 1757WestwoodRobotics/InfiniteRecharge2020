import wpilib
from wpilib import SmartDashboard
from wpilib.command import TimedCommand
from wpilib.interfaces import GenericHID
import subsystems

class DriveForward(TimedCommand):
    '''
    Command to drive robot forward without user control

    Parameters:

    Output: Motor output from -1 to 1; if not specified, default is 1

    Timeout: Time in seconds that the command runs for ; if not specified, deafault is 2
    '''

    def __init__(self, output = 1, timeout = 2):
        TimedCommand.__init__(self, "Drive Forward", timeout)
        self.requires(subsystems.team1757Subsystems.drivetrain)

        self.timeout = timeout
        self.output = output

    def execute(self):
        
        subsystems.team1757Subsystems.drivetrain.arcadeDrive(self.output, 0, False)
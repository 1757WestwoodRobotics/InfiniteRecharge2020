import wpilib
from wpilib import Solenoid
from wpilib.command import InstantCommand
import subsystems

class SetSolenoid(InstantCommand):
    '''
    Command to set a solenoid to a desired position

    Parameters:

    Solenoid: The solenoid from the pneumatics subsystem that will be manipulated

    Enabled: If true, the solenoid is extended, if false, the solenoid is retracted
    '''

    def __init__(self, solenoid, enabled):
        InstantCommand.__init__(self, "Set Solenoid")
        
        self.solenoid = solenoid
        self.enabled = enabled

    def initialize(self):
        self.solenoid.set(self.enabled)

    def isFinished(self):
        return True
import wpilib
from wpilib import Solenoid
from wpilib.command import InstantCommand
import subsystems

class SetSolenoid(InstantCommand):
    '''
    Command to set a solenoid to a desired position

    Parameters:

    Solenoid: The solenoid from the pneumatics subsystem that will be manipulated

    Position: Position to set the solenoid to: DoubleSolenoid.Value.kForward/kReverse/kOff
    '''

    def __init__(self, solenoid, enabled):
        InstantCommand.__init__(self, "Set Solenoid")
        
        self.solenoid = solenoid
        self.enabled = enabled

    def initialize(self):
        self.solenoid.set(self.enabled)

    def isFinished(self):
        return False
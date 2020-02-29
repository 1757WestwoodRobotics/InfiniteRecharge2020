import wpilib
from wpilib.command import InstantCommand
import subsystems

class SetDoubleSolenoid(InstantCommand):
    '''
    Command to set a double solenoid to a desired position

    Parameters:

    Solenoid: The double solenoid from the that will be manipulated

    Modes: DoubleSolenoid.Value.kForward/kReverse/kOff
    '''

    def __init__(self, solenoid, mode):
        InstantCommand.__init__(self, "Set Double Solenoid")
        
        self.solenoid = solenoid
        self.mode = mode

    def initialize(self):
        self.solenoid.set(self.mode)

    def isFinished(self):
        return True
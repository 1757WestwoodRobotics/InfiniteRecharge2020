import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Command
import subsystems

class SetDoubleSolenoidLoop(Command):
    '''
    Command to set a solenoid to extended and then retracted

    Parameters:

    Solenoid: The double solenoid that will be manipulated
    '''

    def __init__(self, solenoid):
        Command.__init__(self, "Set Double Solenoid Loop")
        
        self.solenoid = solenoid

    def initialize(self):
        self.solenoid.set(DoubleSolenoid.Value.kForward)

    def end(self):
        self.solenoid.set(DoubleSolenoid.Value.kReverse)

    def isFinished(self):
        return False
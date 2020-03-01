import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Command
import subsystems

class SetSolenoidLoop(Command):
    '''
    Command to set a solenoid to extended and then retracted

    Parameters:

    Solenoid: The solenoid from the pneumatics subsystem that will be manipulated
    '''

    def __init__(self, solenoid):
        Command.__init__(self, "Set Solenoid Loop")
        
        self.solenoid = solenoid

    def initialize(self):
        self.solenoid.set(True)

    def end(self):
        self.solenoid.set(False)

    def isFinished(self):
        return False
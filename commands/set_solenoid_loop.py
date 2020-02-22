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

        self.requires(subsystems.team1757Subsystems.pneumatics)
        
        self.solenoid = solenoid

    def initialize(self):
        subsystems.team1757Subsystems.pneumatics.setSolenoid(self.solenoid, True)

    def end(self):
        subsystems.team1757Subsystems.pneumatics.setSolenoid(self.solenoid, False)

    def isFinished(self):
        return False
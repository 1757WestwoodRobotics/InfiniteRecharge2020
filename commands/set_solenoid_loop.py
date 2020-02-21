import wpilib
from wpilib import SmartDashboard, DoubleSolenoid
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
        subsystems.team1757Subsystems.pneumatics.setSolenoid(self.solenoid, DoubleSolenoid.Value.kForward)

    def end(self):
        subsystems.team1757Subsystems.pneumatics.setSolenoid(self.solenoid, DoubleSolenoid.Value.kReverse)

    def isFinished(self):
        return False
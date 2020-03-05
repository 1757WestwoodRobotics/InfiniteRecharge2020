import wpilib
import subsystems
from wpilib.command import Command

class SetLiftBrake(Command):
    '''
    Command to set the brake for the elevator

    Parameters:

    Engaged: If true, the brake will engage, if false, it will retract
    '''
    def __init__(self, engaged):
        Command.__init__(self, "Set Lift Brake")
        
        self.direction = 1 if engaged else -1

    def execute(self):
        subsystems.team1757Subsystems.lift.setLiftBrake(self.direction)

    def end(self):
        subsystems.team1757Subsystems.lift.setLiftBrake(0)

    def isFinished(self):
        return False

import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class RaiseLift(Command):
    '''
    Command to raise the elevator

    Parameters:

    Speed: speed of the motors from 0 to 1
    '''
    def __init__(self, speed):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.lift)
    # need pneumatic subsystem bc of discbrake
    # disengage brake

        self.speed = speed

    def execute(self):
        
        subsystems.team1757Subsystems.lift.setSpeed(self.speed)

        if not subsystems.team1757Subsystems.lift.revstatus:
            subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

    def isFinished(self):
        return False

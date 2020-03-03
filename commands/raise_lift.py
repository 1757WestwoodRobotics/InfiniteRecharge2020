import wpilib
from wpilib import Solenoid
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class RaiseLift(Command):

    def __init__(self):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.lift)
    # need pneumatic subsystem bc of discbrake
    # disengage brake

    def execute(self):

        self.RT = (self.getRobot().oi.xboxController.getRawAxis(3))
        
        subsystems.team1757Subsystems.lift.setSpeed(self.RT)

        if subsystems.team1757Subsystems.lift.fwdstatus:
            subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

# ^ is this enough to keep motors from turning at all costs?

    def isFinished(self):
        return False

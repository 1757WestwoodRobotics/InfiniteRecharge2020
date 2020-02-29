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
        subsystems.team1757Subsystems.lift.lift1.setSpeed(1)
            
        if subsystems.team1757Subsystems.lift.fwdstatus:
            subsystems.team1757Subsystems.lift.lift1.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.lift1.setSpeed(0)

        # engage brake *****make sure motors are never running while brake is on!

    def isFinished(self):
        return False

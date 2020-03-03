import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class LowerLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "LowerLift")

        self.requires(subsystems.team1757Subsystems.lift)

        self.speed = speed
    # need pneumatic subsystem bc of discbrake
    # disengage brake

    def execute(self):
        subsystems.team1757Subsystems.lift.setSpeed(-self.speed)
            
        if subsystems.team1757Subsystems.lift.revstatus:
            subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

        # engage brake *****make sure motors are never running while brake is on!

    def isFinished(self):
        return False
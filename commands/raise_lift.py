import wpilib
from wpilib import Solenoid
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class RaiseLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.lift)

        self.speed = speed

    def execute(self):
        subsystems.team1757Subsystems.lift.setSpeed(self.speed)
            
        if subsystems.team1757Subsystems.lift.fwdstatus:
            subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

# ^ is this enough to keep motors from turning at all costs?

    def isFinished(self):
        return False

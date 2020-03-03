import wpilib
from wpilib import Solenoid
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class LowerLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "LowerLift")

        self.requires(subsystems.team1757Subsystems.lift)

        self.speed = speed
   
    def execute(self):
        subsystems.team1757Subsystems.lift.setSpeed(-self.speed)
            
        if subsystems.team1757Subsystems.lift.revstatus:
            subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

    def isFinished(self):
        return False
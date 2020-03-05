import wpilib
import subsystems
from wpilib.command import Command

class SetLiftBrake(Command):

    def __init__(self, forward: bool = True):
        Command.__init__(self, "Set Lift Brake")
        self.direction = 1 if forward else -1

    def execute(self):
        subsystems.team1757Subsystems.lift.setLiftBrake(self.direction)

    def end(self):
        subsystems.team1757Subsystems.lift.setLiftBrake(0)

    def isFinished(self):
        return False

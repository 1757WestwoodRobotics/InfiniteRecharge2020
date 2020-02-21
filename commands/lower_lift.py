#    Uses the Lifter subsystem to lower the lifter until the lower limit is reached (and keep it there)
import wpilib
from wpilib.command import Command
import subsystems

class LowerLift(Command):

    def __init__(self):
        Command.__init__(self, "LowerLift")

        self.requires(subsystems.team1757Subsystems.Lift)

    def execute(self):
        # self.speed = self.getRobot()
        # self.rotation = self.getRobot()
    
        while (value < self.lowerlimitvalue):
            subsystems.team1757Subsystems.Lift.set(self.speed, self.rotation)
        else:
            self.speed=0
            self.rotation=0
            subsystems.team1757Subsystems.Lift.set(self.speed, self.rotation)
            self.done = True

    def isFinished(self):
        if  self.done == True:
            return True
        else:
            return False
#  Uses the Lifter subsystem to raise the lifter until the upper limit is reached (and keep it there)
import wpilib
from wpilib.command import Command
import subsystems

class RaiseLift(Command):

    def __init__(self):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.Lift)

    def execute(self):
        # self.speed = self.getRobot()
        # self.rotation = self.getRobot()
    
        while (value < self.upperlimitvalue):
            subsystems.team1757Subsystems.Lift.setSpeed(self.speed, self.rotation)
        else:
            self.speed=0
            self.rotation=0
            subsystems.team1757Subsystems.Lift.setSpeed(self.speed, self.rotation)
            self.done = True

    def isFinished(self):
        if  self.done == True:
            return True
        else:
            return False


            # The "execute" and "isFinished" methods of the command is called repeatedly by the command scheduler while the command is active, so instead of using a while loop to check the limit switches consider doing the check in "isFinished" without a while loop.

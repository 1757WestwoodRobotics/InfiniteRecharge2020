# so instead of using a while loop to check the limit switches consider doing the check in "isFinished" without a while loop.
#  Uses the Lifter subsystem to raise the lifter until the upper limit is reached (and keep it there)
import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can
from subsystems.lift import Lift

class RaiseLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.lift)
        self.forwardLimitSwitch = wpilib.DigitalInput(1)
        
        self.lift1 = WPI_TalonSRX(Can.lift1)
        self.speed = speed

    def execute(self):
        # if button is pressed (in oi.py), motors will run when upper limit value is not reached, if it is, motors will stop
        while (Lift.fwdstatus < self.upperlimitvalue):  
            subsystems.team1757Subsystems.lift.setSpeed(self.speed)
            
        self.speed = 0
        subsystems.team1757Subsystems.lift.setSpeed(self.speed)
        self.done = True

    def isFinished(self):
        if  self.done == True:
            return True
        else:
            return False
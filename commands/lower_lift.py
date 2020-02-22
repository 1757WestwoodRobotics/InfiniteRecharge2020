#    Uses the Lifter subsystem to lower the lifter until the lower limit is reached (and keep it there)
import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class LowerLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "LowerLift")

        self.requires(subsystems.team1757Subsystems.Lift)
        self.reverseLimitSwitch = wpilib.DigitalInput(2)
        
        self.lift1 = WPI_TalonSRX(Can.lift1)
        self.speed = speed

    def execute(self):
        
        while (self.revstatus < self.lowerlimitvalue):  
            subsystems.team1757Subsystems.Lift.setSpeed(self.speed)
            
        self.speed = 0
        subsystems.team1757Subsystems.Lift.setSpeed(self.speed)
        self.done = True

    def isFinished(self):
        if  self.done == True:
            return True
        else:
            return False
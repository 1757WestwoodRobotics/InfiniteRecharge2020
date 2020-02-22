#  Uses the Lifter subsystem to raise the lifter until the upper limit is reached (and keep it there)
import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class RaiseLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.lift)
        self.forwardLimitSwitch = wpilib.DigitalInput(1)
        
        self.lift1 = WPI_TalonSRX(Can.lift1)
        self.speed = speed

    def execute(self):
        # if button is pressed (in oi.py), motors will run when upper limit value is not reached, if it is, motors will stop
        if subsystems.team1757Subsystems.lift.fwdstatus < subsystems.team1757Subsystems.lift.upperlimitvalue:
            subsystems.team1757Subsystems.lift.setSpeed(self.speed)
        else:    
            self.speed = 0
            subsystems.team1757Subsystems.lift.setSpeed(self.speed)
    
    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

    def isFinished(self):
        return False
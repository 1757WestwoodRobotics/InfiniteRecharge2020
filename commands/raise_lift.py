#  Uses the Lifter subsystem to raise the lifter until the upper limit is reached (and keep it there)
import wpilib
from wpilib.command import Command
import subsystems

class RaiseLift(Command):

    def __init__(self):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.Lift)

    def execute(self):
        self.speed.set()
        self.rotation.set()
    
        '''if button is pressed , motors will run when upper limit value is not reached, if it is, motors will stop'''

        while (self.fwdstatus < self.upperlimitvalue):  
            subsystems.team1757Subsystems.Lift.set(self.speed, self.rotation)
        
        self.speed=0
        self.rotation=0
        subsystems.team1757Subsystems.Lift.set(self.speed, self.rotation)
        self.done = True

    def isFinished(self):
        if  self.done == True:
            return True
        else:
            return False


            # The "execute" and "isFinished" methods of the command is called repeatedly by the command scheduler while the command is active, 
            # so instead of using a while loop to check the limit switches consider doing the check in "isFinished" without a while loop.

    def robotInit(self):
        self.forwardLimitSwitch = wpilib.DigitalInput(1)
        self.reverseLimitSwitch = wpilib.DigitalInput(2)
        self.joystick1 = wpilib.Joystick(1)
        self.motor = wpilib.Talon(1)

    def teleopPeriodic(self):
        output = self.Joystick1.getY()
        if self.forwardLimitSwitch.get():
            output = min(0, output)
        elif self.reverseLimitSwitch.get():
            output = max(0, output)

        motor.set(output)

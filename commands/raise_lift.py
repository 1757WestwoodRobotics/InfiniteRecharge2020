import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class RaiseLift(Command):

    def __init__(self, speed):
        Command.__init__(self, "RaiseLift")

        self.requires(subsystems.team1757Subsystems.lift)
        
        self.lift1 = WPI_TalonSRX(Can.lift1)
        self.speed = speed

    def execute(self):
        
        if subsystems.team1757Subsystems.lift.fwdstatus:
            subsystems.team1757Subsystems.lift.setSpeed(self.speed)
        else:    
            self.speed = 0
            subsystems.team1757Subsystems.lift.setSpeed(self.speed)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

    def isFinished(self):
        return False

'''
configure motor controller to turn on limit switch checking

if limit/target position not yet reached, motors run at a set speed

encoder counts is read as a position, multiply factor by position in inches
'''
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
# .get = isllimitswtichclosed aka fwdstatus?
        motor.set(output)

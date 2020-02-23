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
    # need pneumatic subsystem bc of discbrake
        
        self.speed = speed

    def execute(self):
        # if limit/target position not yet reached, motors run at a set speed    

        # subsystems.team1757Subsystems.lift.lift1
        
        if subsystems.team1757Subsystems.lift.fwdstatus:
            self.speed = 1
            subsystems.team1757Subsystems.lift.lift1.setSpeed(self.speed)

        else:    
            self.speed = 0
            subsystems.team1757Subsystems.lift.lift1.setSpeed(self.speed)

    # alternative way to do it idk if either works though
        # if self.fwdstatus():
        #     speed = min(0, speed)
        # elif self.revstatus():
        #     speed = max(0, speed)

    def end(self):
        subsystems.team1757Subsystems.lift.lift1.setSpeed(0)

    def isFinished(self):
        return False

'''
disengage brake
set speed(up)
when up limit
setspeed(0)
engage brake
'''
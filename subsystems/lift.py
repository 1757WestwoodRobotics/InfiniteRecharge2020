# get value, if it exceeds upper limit value, print limit switch value
import wpilib
from ctre import WPI_TalonSRX
from robotmap import Can
from wpilib.command import Subsystem

class Lift(Subsystem):

    def __init__(self):
        Subsystem.__init__(self, "Lift")
        # lift1 = motor 11
        self.lift1 = WPI_TalonSRX(Can.lift1)
        self.upperlimitvalue= 21
        self.lowerlimitvalue= 0

        self.fwdstatus = self.lift1.isFwdLimitSwitchClosed()
        self.revstatus = self.lift1.isRevLimitSwitchClosed()
        #isFwdLimitSwitchClosed get the status of limit switch (returns an int)
    
    def setSpeed(self, speed):
        self.lift1.set(speed)

    def periodic(self):
        #used to read the upper limit switch value from the motor
        if self.fwdstatus >= self.upperlimitvalue:
            print(self.fwdstatus)
    
        if self.revstatus <= self.lowerlimitvalue:
            print(self.revstatus)
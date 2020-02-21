import wpilib
from ctre import WPI_TalonSRX
from robotmap import Can
from wpilib.command import Subsystem

class Lift(Subsystem):

    def __init__(self):
        Subsystem.__init__(self, "Lift")

        self.lift1 = WPI_TalonSRX(Can.lift1)
        # self.reverseLimitSwitch = wpilib.DigitalInput(1)
        self.upperlimitvalue= 21
        self.lowerlimitvalue= 0

        self.x = self.lift1.isFwdLimitSwitchClosed()
        self.y = self.lift1.isRevLimitSwitchClosed()
        #isFwdLimitSwitchClosed get the status of limit switch (returns an int??)
    
    def setSpeed(self, speed):
        self.lift1.set(speed)

    def periodic(self):
        Subsystem.periodic(self, "Lift")
    
        '''get value, if it exceeds upper limit value, print limit switch value'''
        #used to read the upper limit switch value from the motor
        if self.x >= self.upperlimitvalue:
            print(self.x)
    
        if self.y <= self.lowerlimitvalue:
            print(self.y)
    
    # def isAtUpperLimit(self, value, output):
    #     if value >= self.upperlimitvalue:
    #         if self.reverseLimitSwitch.get():
    #             output = max(0, output)
    #             self.lift1.set(output)

    # def isAtLowerLimit(self, value, output):
    #     if value <= self.lowerlimitvalue:
    #         if self.reverseLimitSwitch.get():
    #             output = max(0, output)
    #             self.lift1.set(output)
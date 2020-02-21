import wpilib
from ctre import WPI_TalonSRX
from robotmap import Can
from wpilib.command import Subsystem

class Lift(Subsystem):

    def __init__(self):
        Subsystem.__init__(self, "Lift")

        self.lift1 = WPI_TalonSRX(Can.lift1)
        # lift1=motor
        self.reverseLimitSwitch = wpilib.DigitalInput(1)
        # 20 arbitrary value
        self.upperlimitvalue= 21
        self.lowerlimitvalue= 0
        # configReverseLimitSwitchSource()
        self.x = self.lift1.isFwdLimitSwitchClosed()
        self.y = self.lift1.isRevLimitSwitchClosed()
        #isFwdLimitSwitchClosed get the status of limit switch (returns an int??)
    def periodic(self):
        Subsystem.periodic(self, "Lift")
        
        
        print(self.x)
        print(self.y)
   

    def setSpeed(self, speed):
        self.lift1.set(speed)

#used to read the upper limit switch value from the motor
    def isAtUpperLimit(self, value, output):
        if value >= self.upperlimitvalue:
            if self.reverseLimitSwitch.get():
                output = max(0, output)
                return self.lift1.set(output)

#used to read the lower limit switch value from the motor
    def isAtLowerLimit(self, value, output):
        if value <= self.lowerlimitvalue:
            if self.reverseLimitSwitch.get():
                output = max(0, output)
                return self.lift1.set(output)
import wpilib
from ctre import WPI_TalonSRX
from robotmap import Can
from wpilib.command import Subsystem

class Lift(Subsystem):

    def __init__(self):
        Subsystem.__init__(self, "Lift")

        self.falconmotor = WPI_TalonSRX(Can.falconmotor)
        # self.motor = wpilib.Talon(1)
        self.reverseLimitSwitch = wpilib.DigitalInput(1)
        # self.upperlimitvalue=   need to measure these
        # self.lowerlimitvalue=

    def setSpeed(self, speed):
        self.falconmotor.set(speed)

#used to read the upper limit switch value from the motor
    def isAtUpperLimit(self, upperlimitvalue, value, output):
        if value >= self.upperlimitvalue:
            if self.reverseLimitSwitch.get():
                output = max(0, output)
                return self.falconmotor.set(output)

#used to read the lower limit switch value from the motor
    def isAtLowerLimit(self, lowerlimitvalue, value, output):
        if value >= self.lowerlimitvalue:
            if self.reverseLimitSwitch.get():
                output = max(0, output)
                return self.falconmotor.set(output)


# For programming the Falcon 500 motor, the TalonSRX class is used_Looking at the page, 
# we can see that it has _as its base class. 
# Consider using the methods "isFwdLimitSwitchClosed" and "isRevLimitSwitchClosed" to get the status.

'''
notes for later:
why is there 2 drives in "from wpilib import drive, SpeedControllerGroup, drive" in drivetrain subsystem
what is lift 1 and lift 2 in robotmap
need values for upper and lower limits
-Tif
'''
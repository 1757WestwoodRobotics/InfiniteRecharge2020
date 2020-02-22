import wpilib
from ctre import WPI_TalonSRX
from ctre import ControlMode
from robotmap import Can
from wpilib.command import Subsystem
from math import pi

class Lift(Subsystem):

    sprocketdiameter = 3.341
    gearratio = 14.2
    inch = 1
    encodercounts = 2048

    sprocketcirc = sprocketdiameter * pi
    sprocketrot = inch / sprocketcirc 
    motorrot = gearratio * sprocketrot
    inches_to_encodercounts_factor = encodercounts * motorrot

    def __init__(self):
        Subsystem.__init__(self, "Lift")
        # lift1 = motor 11
        self.lift1 = WPI_TalonSRX(Can.lift1)
        self.upperlimitvalue = inches_to_encodercounts_factor
        self.lowerlimitvalue = 0

    def setSpeed(self, speed):
        self.lift1.set(speed)

    def setPosition(self, position_in_inches):
        position_in_encoder_counts = position_in_inches * inches_to_encodercounts_factor
        self.lift1.set(ControlMode.Position, position_in_encoder_counts)
        
    def periodic(self):
        #used to read the limit switch value from the motor

        self.fwdstatus = self.lift1.isFwdLimitSwitchClosed()
        self.revstatus = self.lift1.isRevLimitSwitchClosed()
        #get the status of limit switch (returns an int)

        if fwdstatus:
            print(self.fwdstatus)
        if revstatus:
            print(self.revstatus)
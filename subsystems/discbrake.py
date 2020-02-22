import wpilib
from wpilib import Solenoid
from robotmap import Can, PCM
from wpilib.command import Subsystem

class DiscBrake(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Disc Brake")
    
        self.discBrake = Solenoid(Can.PCM, PCM.DiscBrake)
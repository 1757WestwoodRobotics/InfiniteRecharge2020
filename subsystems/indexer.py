import wpilib
from wpilib import Solenoid
from robotmap import Can, PCM
from wpilib.command import Subsystem

class Indexer(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Indexer")

        self.indexer1 = Solenoid(Can.PCM, PCM.Indexer1)
        self.indexer2 = Solenoid(Can.PCM, PCM.Indexer2)

    def setSolenoid(self, solenoid, enabled):
        solenoid.set(enabled)
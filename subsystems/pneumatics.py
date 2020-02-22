import wpilib
from wpilib import Compressor, Solenoid
from robotmap import PCM
from wpilib.command import Subsystem
from commands.stop_compress import StopCompress

class Pneumatics(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Pneumatics")

        self.compressor = Compressor()

        self.controlPanel = Solenoid(PCM.ControlPanel)
        self.collectorDeploy = Solenoid(PCM.Collector)
        self.discBrake = Solenoid(PCM.DiscBrake)
        self.indexer1 = Solenoid(PCM.Indexer1)
        self.indexer2 = Solenoid(PCM.Indexer2)

    def setCompressor(self, enabled):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()

    def setSolenoid(self, solenoid, enabled):
        solenoid.set(enabled)
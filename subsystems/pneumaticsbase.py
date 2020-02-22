import wpilib
from wpilib import Compressor, Solenoid
from robotmap import Can, PCM
from wpilib.command import Subsystem
from commands.stop_compress import StopCompress

class PneumaticsBase(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Pneumatics Base")

        self.compressor = Compressor()

        # self.controlPanel = Solenoid(Can.PCM, PCM.ControlPanel)
        # self.collectorDeploy = Solenoid(Can.PCM, PCM.Collector)
        # self.discBrake = Solenoid(Can.PCM, PCM.DiscBrake)
        # self.indexer1 = Solenoid(Can.PCM, PCM.Indexer1)
        # self.indexer2 = Solenoid(Can.PCM, PCM.Indexer2)

    def setCompressor(self, enabled):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()
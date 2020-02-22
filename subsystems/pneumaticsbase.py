import wpilib
from wpilib import Compressor, Solenoid
from robotmap import Can, PCM
from wpilib.command import Subsystem
from commands.stop_compress import StopCompress

class PneumaticsBase(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Pneumatics Base")

        self.compressor = Compressor()

        # self.collectorDeploy = Solenoid(Can.PCM, PCM.Collector)

    def setCompressor(self, enabled):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()
import wpilib
from wpilib import Compressor, DoubleSolenoid
from robotmap import PCM1
# from robotmap import PCM2
from wpilib.command import Subsystem
from commands.stop_compress import StopCompress

class Pneumatics(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Pneumatics")

        self.compressor = Compressor()

        self.controlPanel = DoubleSolenoid(PCM1.ControlPanelF, PCM1.ControlPanelR)
        # self.collectordeploy = DoubleSolenoid(PCM2.CollectorF, PCM2.CollectorR)
        self.discBrake = DoubleSolenoid(PCM1.DiscBrakeF, PCM1.DiscBrakeR)
        self.indexer1 = DoubleSolenoid(PCM1.Indexer1F, PCM1.Indexer1R)
        self.indexer2 = DoubleSolenoid(PCM1.Indexer2F, PCM1.Indexer2R)
    
    def setCompressor(self, enabled):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()

    def setSolenoid(self, solenoid, position):
        solenoid.set(position)
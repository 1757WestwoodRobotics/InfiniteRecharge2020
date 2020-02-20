import wpilib
from wpilib import Compressor, DoubleSolenoid
from robotmap import PCM1
from wpilib.command import Subsystem

class Pneumatics(Subsystem):
    def __init__(self):
        self.compressor = Compressor(PCM1.Compressor)
        self.discbrake = DoubleSolenoid(PCM1.DiscBrakeF, PCM1.DiscBrakeB)
        self.ballRelease1 = DoubleSolenoid(PCM1.BallRelease1F, PCM1.BallRelease1B)
        self.ballRelease2 = DoubleSolenoid(PCM1.BallRelease2F, PCM1.BallRelease2B)
        #self.frontRakeDeploy = wpilib.DoubleSolenoid(PneumaticsConst.FrontRakeDeploy[0], PneumaticsConst.FrontRakeDeploy[1])

    def setCompressor(self, enabled = False):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()
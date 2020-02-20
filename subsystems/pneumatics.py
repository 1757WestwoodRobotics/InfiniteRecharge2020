import wpilib
from wpilib import Compressor, DoubleSolenoid
from robotmap import PCM1
from wpilib.command import Subsystem

class Pneumatics(Subsystem):
    def __init__(self):
        self.compressor = Compressor(0)
        # self.discbrake = DoubleSolenoid(PCM1.DiscBrake[0], PCM1.DiscBrake[1])
        # self.ballRelease1 = DoubleSolenoid(PCM1.BallRelease1[0], PCM1.BallRelease1[1])
        # self.ballRelease2 = DoubleSolenoid(PCM1.BallRelease2[0], PCM1.BallRelease2[1])
        #self.frontRakeDeploy = wpilib.DoubleSolenoid(PneumaticsConst.FrontRakeDeploy[0], PneumaticsConst.FrontRakeDeploy[1])

    def setCompressor(self, enabled = False):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()
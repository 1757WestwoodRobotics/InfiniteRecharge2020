import wpilib
from robotmap import PneumaticsConst
from wpilib.command import Subsystem

class Pneumatics(Subsystem):
    def __init__(self):
        self.compressor = wpilib.Compressor(PneumaticsConst.Compressor)
        self.discbrake = wpilib.DoubleSolenoid(PneumaticsConst.DiscBrake[0], PneumaticsConst.DiscBrake[1])
        self.ballRelease1 = wpilib.DoubleSolenoid(PneumaticsConst.BallRelease1[0], PneumaticsConst.BallRelease1[1])
        self.ballRelease2 = wpilib.DoubleSolenoid(PneumaticsConst.BallRelease2[0], PneumaticsConst.BallRelease2[1])
        #self.frontRakeDeploy = wpilib.DoubleSolenoid(PneumaticsConst.FrontRakeDeploy[0], PneumaticsConst.FrontRakeDeploy[1])

    def setCompressor(self, enabled: bool = False):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()
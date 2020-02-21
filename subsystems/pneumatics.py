import wpilib
from wpilib import Compressor, DoubleSolenoid
from robotmap import PCM1
from wpilib.command import Subsystem
from commands.stop_compress import StopCompress

class Pneumatics(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Pneumatics")

        self.compressor = Compressor(PCM1.Compressor)
        
        self.discbrake = DoubleSolenoid(PCM1.DiscBrakeF, PCM1.DiscBrakeB)
        self.ballRelease1 = DoubleSolenoid(PCM1.BallRelease1F, PCM1.BallRelease1B)
        self.ballRelease2 = DoubleSolenoid(PCM1.BallRelease2F, PCM1.BallRelease2B)
        #self.frontRakeDeploy = wpilib.DoubleSolenoid(PneumaticsConst.FrontRakeDeploy[0], PneumaticsConst.FrontRakeDeploy[1])
    
    def setCompressor(self, enabled):
        if enabled:
            self.compressor.start()
        else:
            self.compressor.stop()

    def setSolenoid(self, solenoid, position):
        solenoid.set(position)
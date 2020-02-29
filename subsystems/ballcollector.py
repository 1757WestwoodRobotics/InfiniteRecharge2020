import wpilib
from wpilib import DoubleSolenoid
from ctre import WPI_TalonSRX
from robotmap import Can, PCM
from wpilib.command import Subsystem
from commands.spin_ball_collector import SpinBallCollector

class BallCollector(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Ball Collector")

        self.collectormotor = WPI_TalonSRX(Can.collector)
        self.collectorsolenoid = DoubleSolenoid(Can.PCM, PCM.CollectorF, PCM.CollectorR)

    def spin(self, speed):
        self.collectormotor.set(speed)

    def initDefaultCommand(self):
        self.setDefaultCommand(SpinBallCollector(1))
import wpilib
from wpilib import drive, SpeedControllerGroup
from ctre import WPI_TalonSRX
from robotmap import *
from networktables import NetworkTablesInstance

class Robot(wpilib.TimedRobot):

    def robotInita(self):
        self.balltalon1 = WPI_TalonSRX(motorcontrollerports["ballshooter1"])
        self.balltalon2 = WPI_TalonSRX(motorcontrollerports["ballshooter2"])
        self.leftFront = WPI_TalonSRX(motorcontrollerports["leftFront"])
        self.rightFront = WPI_TalonSRX(motorcontrollerports["rightFront"])
        self.leftBack = WPI_TalonSRX(motorcontrollerports["leftBack"])
        self.rightBack = WPI_TalonSRX(motorcontrollerports["rightBack"])

        NetworkTablesInstance.intialize(server="10.17.57.2")
        self.sd = NetworkTablesInstance.getTable("SmartDashboard")
    def teleopPeriodic(self):
        self.leftFrontSpeed = self.sd.getNumber("leftFront", 0)
        self.rightFrontSpeed = self.sd.getNumber("rightFront", 0)
        self.leftBackSpeed = self.sd.getNumber("leftBack", 0)
        self.rightBackSpeed = self.sd.getNumber("rightBack", 0)

        self.leftFront.set(self.leftFrontSpeed)
        self.rightFront.set(self.rightFrontSpeed)
        self.leftBack.set(self.leftBackSpeed)
        self.rightBack.set(self.rightBackSpeed)
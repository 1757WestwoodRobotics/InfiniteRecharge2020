import wpilib
from wpilib import RobotDrive, SpeedControllerGroup, drive
from ctre import WPI_TalonSRX
from robot import *
from wpilib.command.subsystem import Subsystem

class Drivetrain(Subsystem):
    
    def init(self):
        self.leftFront = WPI_TalonSRX(can["leftFront"])
        self.rightFront = WPI_TalonSRX(can["rightFront"])
        self.leftBack = WPI_TalonSRX(can["leftBack"])
        self.rightBack = WPI_TalonSRX(can["rightBack"])

        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)
        self.leftDrive = SpeedControllerGroup(self.leftFront, self.leftBack)

        self.differentialDrive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

        self.speed = self.xboxController.getY(GenericHID.Hand.kLeft)
        self.rotation = self.xboxController.getX(GenericHID.Hand.kRight)

    def xboxControllerDrive(self):
        self.differentialDrive.arcadeDrive(self.speed, self.rotation, True)
import wpilib
from wpilib import RobotDrive, SpeedControllerGroup, drive
from ctre import WPI_TalonSRX
from wpilib.interfaces import GenericHID
from robotmap import *
from wpilib.command import Subsystem
from commands.drive import Drive

class Drivetrain(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(name=Drivetrain)

        self.leftFront = WPI_TalonSRX(Can.LeftFront)
        self.rightFront = WPI_TalonSRX(Can.RightFront)
        self.leftBack = WPI_TalonSRX(Can.LeftBack)
        self.rightBack = WPI_TalonSRX(Can.RightBack)

        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)
        self.leftDrive = SpeedControllerGroup(self.leftFront, self.leftBack)

        self.differentialDrive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

    def arcadeDrive(self, speed, rotation):
        self.differentialDrive.arcadeDrive(speed, rotation, True)

    def tankDrive(self, leftSpeed, rightSpeed):
        self.differentialDrive.tankDrive(leftSpeed, rightSpeed, True)

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive())
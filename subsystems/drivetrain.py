import wpilib
from wpilib import RobotDrive, SpeedControllerGroup, drive
from ctre import WPI_TalonSRX
from wpilib.interfaces import GenericHID
from robotmap import *
from wpilib.command.subsystem import Subsystem

class Drivetrain(Subsystem):
    
    def __init__(self):
        super().__init__(name=Drivetrain)

        self.leftFront = WPI_TalonSRX(can["leftFront"])
        self.rightFront = WPI_TalonSRX(can["rightFront"])
        self.leftBack = WPI_TalonSRX(can["leftBack"])
        self.rightBack = WPI_TalonSRX(can["rightBack"])

        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)
        self.leftDrive = SpeedControllerGroup(self.leftFront, self.leftBack)

        self.differentialDrive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)
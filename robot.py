import wpilib
from wpilib import drive, SpeedControllerGroup, RobotDrive, XboxController, interfaces
from wpilib.interfaces import GenericHID
from ctre import WPI_TalonSRX
from robotmap import *
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        self.leftFront = WPI_TalonSRX(motorcontrollerports["leftFront"])
        self.rightFront = WPI_TalonSRX(motorcontrollerports["rightFront"])
        self.leftBack = WPI_TalonSRX(motorcontrollerports["leftBack"])
        self.rightBack = WPI_TalonSRX(motorcontrollerports["rightBack"])

        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)
        self.leftDrive = SpeedControllerGroup(self.leftFront, self.rightFront)

        self.differentialDrive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

        self.ballTalon1 = WPI_TalonSRX(motorcontrollerports["ballshooter1"])
        self.ballTalon2 = WPI_TalonSRX(motorcontrollerports["ballshooter2"])

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")

        self.xboxController = XboxController(0)

    def teleopPeriodic(self):
        self.speed = self.xboxController.getY(GenericHID.Hand.kLeft)
        self.rotation = self.xboxController.getX(GenericHID.Hand.kRight)
        
        self.differentialDrive.arcadeDrive(self.speed, self.rotation, True)

if __name__ == "__main__":
    wpilib.run(Robot)
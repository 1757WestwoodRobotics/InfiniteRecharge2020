import wpilib
from wpilib import drive, SpeedControllerGroup, RobotDrive
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

        self.balltalon1 = WPI_TalonSRX(motorcontrollerports["ballshooter1"])
        self.balltalon2 = WPI_TalonSRX(motorcontrollerports["ballshooter2"])

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")
        self.sd.putBoolean("Run Motor Forward", False)
        self.sd.putBoolean("Run Motor Backward", False)
    
    def teleopPeriodic(self):
        self.runMotorForward = self.sd.getBoolean("Run Motor Forward", False)
        self.runMotorBackward = self.sd.getBoolean("Run Motor Backward", False)

        if self.runMotorForward:
            self.leftFront.set(1)
            self.rightFront.set(1)
            self.leftBack.set(-1)
            self.rightBack.set(-1)
        elif self.runMotorBackward:
            self.leftFront.set(-1)
            self.rightFront.set(-1)
            self.leftBack.set(1)
            self.rightBack.set(1)
        else:
            self.leftFront.set(0)
            self.rightFront.set(0)
            self.leftBack.set(0)
            self.rightBack.set(0)

if __name__ == "__main__":
    wpilib.run(Robot)
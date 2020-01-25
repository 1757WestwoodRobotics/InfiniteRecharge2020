import wpilib
from ctre import WPI_TalonSRX
from wpilib import drive, SpeedControllerGroup, RobotDrive, XboxController, interfaces, SerialPort
from wpilib.interfaces import GenericHID
# from ctre import WPI_TalonSRX
# import oi
# from subsystems.drivetrain import *
# from subsystems.ballshooter import *
# from subsystems.controlPanel import *
from robotmap import *
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        self.leftBack = WPI_TalonSRX(can["leftBack"])
        self.leftFront = WPI_TalonSRX(can["leftFront"])
        self.rightBack = WPI_TalonSRX(can["rightBack"])
        self.rightFront = WPI_TalonSRX(can["rightFront"])

        self.leftDrive = SpeedControllerGroup(self.leftBack, self.leftFront)
        self.rightDrive = SpeedControllerGroup(self.rightBack, self.rightFront)

        self.drive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

        self.joystick = XboxController(0)
        # Drivetrain.init()
        # Ballshooter.init()
        # ControlPanel.init()

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")

        # self.serial = SerialPort(9600, SerialPort.Port.kUSB)

        # self.color = int(self.serial.readString())

    def teleopPeriodic(self):

        self.drive.arcadeDrive(self.joystick.getX(hand=GenericHID.Hand.kLeft), self.joystick.getY())
        # Drivetrain.xboxControllerDrive()

        # if XboxController.getAButton():
        #     robotInit.ControlPanelSpin(colors["blue"])

if __name__ == "__main__":
    wpilib.run(Robot)

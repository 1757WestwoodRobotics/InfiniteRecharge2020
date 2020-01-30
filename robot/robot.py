import wpilib
from ctre import WPI_TalonSRX
from rev.color import ColorSensorV3
from wpilib import drive, SpeedControllerGroup, XboxController, interfaces, SerialPort
from wpilib.interfaces import GenericHID
# import oi
from robot.robotmap import *
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        # self.leftBack = WPI_TalonSRX(can["leftBack"])
        # self.leftFront = WPI_TalonSRX(can["leftFront"])
        # self.rightBack = WPI_TalonSRX(can["rightBack"])
        # self.rightFront = WPI_TalonSRX(can["rightFront"])

        # self.leftDrive = SpeedControllerGroup(self.leftBack, self.leftFront)
        # self.rightDrive = SpeedControllerGroup(self.rightBack, self.rightFront)

        # self.drive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

        # self.joystick = XboxController(0)

        self.color_sensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

        # Drivetrain.init()
        # Ballshooter.init()
        # ControlPanel.init()

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")

        # self.serial = SerialPort(9600, SerialPort.Port.kUSB)

        # self.color = int(self.serial.readString())

    def teleopPeriodic(self):

        # self.drive.arcadeDrive(self.joystick.getX(hand=GenericHID.Hand.kLeft), self.joystick.getY())
        # Drivetrain.xboxControllerDrive()

        color = self.color_sensor.getColor()
        self.sd.putNumber("red", color.red)
        self.sd.putNumber("blue", color.blue)
        self.sd.putNumber("green", color.green)

        proximity = self.color_sensor.getProximity()

        self.sd.putNumber("proximity", proximity)

        # if XboxController.getAButton():
        #     robotInit.ControlPanelSpin(colors["blue"])

if __name__ == "__main__":
    wpilib.run(Robot)

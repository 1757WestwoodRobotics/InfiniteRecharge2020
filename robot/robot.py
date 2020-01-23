import wpilib
from wpilib import drive, SpeedControllerGroup, RobotDrive, XboxController, interfaces, SerialPort
from wpilib.interfaces import GenericHID
from ctre import WPI_TalonSRX
import oi
from subsystems.drivetrain import *
from subsystems.ballshooter import *
from subsystems.controlPanel import *
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):

        Drivetrain.init()
        Ballshooter.init()
        ControlPanel.init()

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")

        self.serial = SerialPort(9600, SerialPort.Port.kUSB)

        self.color = int(self.serial.readString())

    def teleopPeriodic(self):

        Drivetrain.xboxControllerDrive()

        if XboxController.getAButton():
            robotInit.ControlPanelSpin(colors["blue"])

if __name__ == "__main__":
    wpilib.run(Robot)

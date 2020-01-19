import wpilib
from wpilib import drive, SpeedControllerGroup, RobotDrive, XboxController, interfaces, SerialPort
from wpilib.interfaces import GenericHID
from ctre import WPI_TalonSRX
from robotmap import *
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

        def ControlPanelSpin(descolor):
            if descolor == self.color:
                self.CPTalon.set(0)
            else:
                self.CPTalon.set(1)

    def teleopPeriodic(self):

        Drivetrain.xboxControllerDrive()

        self.color = int(self.serial.readString())

        if XboxController.getAButton():
            robotInit.ControlPanelSpin(colors["blue"])

if __name__ == "__main__":
    wpilib.run(Robot)
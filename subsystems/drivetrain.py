import wpilib
from wpilib import drive, SpeedControllerGroup, drive
from ctre import WPI_TalonSRX
from wpilib.interfaces import GenericHID

# Team 1757 stuff
from robotmap import Can
from wpilib.command import Subsystem
from commands.arcadedrive import ArcadeDrive
from commands.tankdrive import TankDrive

class Drivetrain(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Drivetrain")

        self.leftFront = WPI_TalonSRX(Can.leftFront)
        self.rightFront = WPI_TalonSRX(1)
        self.leftBack = WPI_TalonSRX(Can.leftBack)
        self.rightBack = WPI_TalonSRX(Can.rightBack)

        self.leftDrive = SpeedControllerGroup(self.leftFront, self.leftBack)
        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)

        self.differentialDrive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

    def arcadeDrive(self, speed, rotation, SquaredInputs):
        self.differentialDrive.arcadeDrive(speed, rotation, SquaredInputs)

    def tankDrive(self, leftSpeed, rightSpeed, SquaredInputs):
        self.differentialDrive.tankDrive(leftSpeed, rightSpeed, SquaredInputs)

    def initDefaultCommand(self):

        # NOTE: To switch between arcade drive and tank drive, switch the default command
        self.setDefaultCommand(ArcadeDrive())
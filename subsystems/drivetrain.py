import wpilib
from wpilib import drive, SpeedControllerGroup
from ctre import WPI_TalonSRX, NeutralMode
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
        self.rightFront = WPI_TalonSRX(Can.rightFront)
        self.leftBack = WPI_TalonSRX(Can.leftBack)
        self.rightBack = WPI_TalonSRX(Can.rightBack)

        self.leftDrive = SpeedControllerGroup(self.leftFront, self.leftBack)
        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)

        self.differentialDrive = drive.DifferentialDrive(self.leftDrive, self.rightDrive)

    def arcadeDrive(self, speed, rotation, SquaredInputs):
        self.differentialDrive.arcadeDrive(speed, rotation, SquaredInputs)

    def tankDrive(self, leftSpeed, rightSpeed, SquaredInputs):
        self.differentialDrive.tankDrive(leftSpeed, rightSpeed, SquaredInputs)

    def setBraking(self, braking):
        if braking:
            self.leftFront.setNeutralMode(NeutralMode.Brake)
            self.rightFront.setNeutralMode(NeutralMode.Brake)
            self.leftBack.setNeutralMode(NeutralMode.Brake)
            self.rightBack.setNeutralMode(NeutralMode.Brake)
        else:
            self.leftFront.setNeutralMode(NeutralMode.Coast)
            self.rightFront.setNeutralMode(NeutralMode.Coast)
            self.leftBack.setNeutralMode(NeutralMode.Coast)
            self.rightBack.setNeutralMode(NeutralMode.Coast)

    def initDefaultCommand(self):

        # NOTE: To switch between arcade drive and tank drive, switch the default command
        self.setDefaultCommand(ArcadeDrive())
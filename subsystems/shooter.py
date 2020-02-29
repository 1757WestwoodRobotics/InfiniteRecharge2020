import wpilib
from wpilib.command import Subsystem
from ctre import WPI_TalonSRX, ControlMode
from robotmap import Can

class Shooter(Subsystem):
    
    def __init__(self):
        Subsystem.__init__(self, "Shooter")
        wpilib.SmartDashboard.putNumber("Desired Shooter Velocity", 15000)
        self.topMotor = WPI_TalonSRX(Can.ballShooterUpper)
        self.bottomMotor = WPI_TalonSRX(Can.ballShooterLower)
        self.bottomMotor.setInverted(True)

    def spinUp(self):
        desired_velocity = wpilib.SmartDashboard.getNumber("Desired Shooter Velocity", 15000)
        self.topMotor.set(ControlMode.Velocity, desired_velocity)
        self.bottomMotor.set(ControlMode.Velocity, desired_velocity)

    def spinDown(self):
        self.topMotor.set(0)
        self.bottomMotor.set(0)
    
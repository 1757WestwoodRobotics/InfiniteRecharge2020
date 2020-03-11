import wpilib
from wpilib import SmartDashboard
from wpilib.command import Subsystem
from ctre import WPI_TalonSRX, ControlMode
from robotmap import Can

class Shooter(Subsystem):
    
    def __init__(self):
        self.spinning = False
        Subsystem.__init__(self, "Shooter")
        wpilib.SmartDashboard.putNumber("Desired Shooter Velocity", 24000)
        self.topMotor = WPI_TalonSRX(Can.ballShooterUpper)
        self.bottomMotor = WPI_TalonSRX(Can.ballShooterLower)
        self.bottomMotor.setInverted(False)

    def spinUp(self):
        desired_velocity = wpilib.SmartDashboard.getNumber("Desired Shooter Velocity", 24000)
        desired_velocity_bottom = wpilib.SmartDashboard.getNumber("Desired Bottom Shooter Velocity", 4000)
        actual_velocity_upper = self.topMotor.getSelectedSensorVelocity()
        actual_velocity_lower = self.bottomMotor.getSelectedSensorVelocity()
        SmartDashboard.putNumber("Actual Velocity Upper", actual_velocity_upper)
        SmartDashboard.putNumber("Actual Velocity Lower", actual_velocity_lower)
        self.topMotor.set(ControlMode.Velocity, desired_velocity)
        self.bottomMotor.set(ControlMode.Velocity, desired_velocity_bottom)

    def spinDown(self):
        self.topMotor.set(0)
        self.bottomMotor.set(0)
    
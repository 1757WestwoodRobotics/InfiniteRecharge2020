import wpilib
import ctre
from networktables import NetworkTables
from ctre import WPI_TalonSRX

class Robot(wpilib.TimedRobot):
    
    def robotInit(self):
        # Define talons
        self.talon5 = WPI_TalonSRX(5)
        self.talon9 = WPI_TalonSRX(9)

        # Init NetworkTables variables
        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")
        self.sd.putNumber("talon5speed", 0)
        self.sd.putNumber("talon9speed", 0)
        self.sd.putNumber("talon5enc", 0)
        self.sd.putNumber("talon9enc", 0)
        self.sd.putNumber("talon5err", 0)
        self.sd.putNumber("talon9err", 0)

        # self.talon5.set(mode=ctre.WPI_TalonSRX.ControlMode.Velocity)
        # self.talon9.set(mode=ctre.WPI_TalonSRX.ControlMode.Velocity)
        # Set PID Constants
        self.talon5.config_kF(0, 0.0517)
        self.talon5.config_kP(0, 0.0)
        self.talon5.config_kI(0, 0.0)
        self.talon5.config_kD(0, 0.0)

        self.talon9.config_kF(0, 0.0602)
        self.talon9.config_kP(0, 0.0)
        self.talon9.config_kI(0, 0.0)
        self.talon9.config_kD(0, 0.0)
    
    def teleopInit(self):
        # Reset speed variables
        self.sd.putNumber("talon5speed", 0)
        self.sd.putNumber("talon9speed", 0)

    def teleopPeriodic(self):
        self.talon5speed = self.sd.getNumber("talon5speed", 0)
        self.talon9speed = self.sd.getNumber("talon9speed", 0)

        # Set talon speeds to networktables variables
        self.talon5.set(mode=ctre.WPI_TalonSRX.ControlMode.Velocity, demand0=self.talon5speed * -1)
        self.talon9.set(mode=ctre.WPI_TalonSRX.ControlMode.Velocity, demand0=self.talon9speed)
        self.sd.putNumber("talon5enc", self.talon5.getQuadratureVelocity())
        self.sd.putNumber("talon9enc", self.talon9.getQuadratureVelocity())
        self.sd.putNumber("talon5err", self.talon5.getClosedLoopError())
        self.sd.putNumber("talon9err", self.talon9.getClosedLoopError())
if __name__ == '__main__':
    wpilib.run(Robot)
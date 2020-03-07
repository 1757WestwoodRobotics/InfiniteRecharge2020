import math
import wpilib
from ctre import WPI_TalonSRX, ControlMode
from wpilib.command import Subsystem

# Team 1757 stuff
from robotmap import Can
from commands.rotate_turret_by_angle import RotateTurretByAngle

class Turret(Subsystem):
    """
    Controls the turret via position PID
    """
    ring_pulley_teeth = 240
    motor_pulley_teeth = 24
    encoder_counts_per_motor_rev = 4096
    encoder_counts_per_ring_rev = encoder_counts_per_motor_rev * (ring_pulley_teeth / motor_pulley_teeth)
    encoder_count_to_degree_factor = 360 / encoder_counts_per_ring_rev
    encoder_count_to_radian_factor = math.pi / encoder_counts_per_ring_rev

    def __init__(self):
        """Instantiates the motor object."""
        Subsystem.__init__(self, "Turret")
        self.motor = WPI_TalonSRX(Can.turret)
        self.motor.setSensorPhase(True)
    
    def periodic(self):
        self.leftstatus = self.motor.isFwdLimitSwitchClosed()
        self.rightstatus = self.motor.isRevLimitSwitchClosed()

    def getPositionDegrees(self):
        return self.motor.getSelectedSensorPosition() * Turret.encoder_count_to_degree_factor

    def getPositionRadians(self):
        return self.motor.getSelectedSensorPosition() * Turret.encoder_count_to_radian_factor

    def getPosition(self):
        return self.motor.getSelectedSensorPosition()

    def setSpeed(self, speed):
        self.motor.set(speed)
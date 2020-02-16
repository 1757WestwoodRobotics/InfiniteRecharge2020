import math
import wpilib
from ctre import WPI_TalonSRX, ControlMode
from wpilib.command import Subsystem

# Team 1757 stuff
from robotmap import Can
from commands.rotate_turret_to_angle import RotateTurretToAngle

class Turret(Subsystem):
    """
    Controls the turret via position PID
    """

    def __init__(self):
        """Instantiates the motor object."""
        Subsystem.__init__(self, "Turret")
        self.motor = WPI_TalonSRX(Can.turret)
        self.encoder = AS5600EncoderPwm(self.motor.getSensorCollection())
        self.lower_limit = -(180 - 45)/360.0
        self.upper_limit =  (180 - 45)/360.0

    def getLowerLimit(self):
        return self.lower_limit

    def getLowerLimitDegrees(self):
        return self.lower_limit * 360.0

    def getLowerLimitRadians(self):
        return self.lower_limit * math.tau

    def getUpperLimit(self):
        return self.upper_limit

    def getUpperLimitDegrees(self):
        return self.upper_limit * 360.0

    def getUpperLimitRadians(self):
        return self.upper_limit * math.tau

    def getPositionDegrees(self):
        return self.encoder.getScaledPositionDegrees()

    def getPositionRadians(self):
        return self.encoder.getScaledPositionRadians()

    def getPosition(self):
        return self.encoder.getScaledPosition()

    def setSpeed(self, speed):
        self.motor.set(speed)

    def initDefaultCommand(self):
        self.setDefaultCommand(RotateTurretToAngle())

class AS5600EncoderPwm:
    INT_MIN = -1 * (2 ** 31)
    SENSOR_MAX = 4096

    def __init__(self, sensorCollection):
        """Instantiates the encoder"""
        self.sensors = sensorCollection
        self.lastValue = AS5600EncoderPwm.INT_MIN

    def getScaledPositionDegrees(self, centered=True):
        return self.getScaledPosition(centered) * 360.0

    def getScaledPositionRadians(self, centered=True):
        return self.getScaledPosition(centered) * math.tau

    def getScaledPosition(self, centered=True):
        scaled_position = self.getPwmPosition() / AS5600EncoderPwm.SENSOR_MAX
        if (centered):
            centered_position = scaled_position - 0.5
            return centered_position
        return scaled_position 

    def getPwmPosition(self):
        raw = self.sensors.getPulseWidthRiseToFallUs()
        if (raw == 0):
            if (self.lastValue == AS5600EncoderPwm.INT_MIN):
                return 0
            return self.lastValue
        actualValue = min(AS5600EncoderPwm.SENSOR_MAX, raw - 128)
        self.lastValue = actualValue
        return actualValue
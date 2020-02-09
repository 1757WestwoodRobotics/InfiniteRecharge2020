import wpilib
from ctre import WPI_TalonSRX, ControlMode
from wpilib.command import Subsystem
from commands.rotate_turret import RotateTurret

class Turret(Subsystem):
    """
    Controls the turret via position PID
    """

    def __init__(self):
        """Instantiates the motor object."""
        Subsystem.__init__(self, "Turret")
        self.motor = WPI_TalonSRX(1)
        self.encoder = AS5600EncoderPwm(self.motor.getSensorCollection())

    def getPosition(self):
        return self.encoder.getScaledPosition()

    def setSpeed(self, speed):
        self.motor.set(speed)
        pass

    def initDefaultCommand(self):
        self.setDefaultCommand(RotateTurret())

class AS5600EncoderPwm:
    INT_MIN = -1 * (2 ** 31)
    SENSOR_MAX = 4096

    def __init__(self, sensorCollection):
        """Instantiates the encoder"""
        self.sensors = sensorCollection
        self.lastValue = AS5600EncoderPwm.INT_MIN

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
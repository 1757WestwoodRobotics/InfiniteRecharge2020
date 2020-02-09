import wpilib
from wpilib.command import Subsystem
from ctre import WPI_TalonSRX

from commands.collect import Collect


class BallCollector(Subsystem):
    """
    This example subsystem controls a single Talon in PercentVBus mode.
    """

    def __init__(self):
        """Instantiates the motor object."""

        Subsystem.__init__(self, "BallCollector")

        self.motor = WPI_TalonSRX(2)

    def setSpeed(self, speed):
        self.motor.set(speed)

    def initDefaultCommand(self):
        self.setDefaultCommand(Collect())

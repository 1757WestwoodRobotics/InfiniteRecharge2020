from wpilib.command import TimedCommand
import subsystems

class SetSpeed(TimedCommand):
    """
    Spins the motor at the given power for a given number of seconds, then
    stops.
    """

    def __init__(self, power, timeoutInSeconds):
        TimedCommand.__init__(self, "Set Speed %d" % power, timeoutInSeconds)

        self.power = power
        self.requires(subsystems.team1757Subsystems.singleMotor)

    def initialize(self):
        subsystems.team1757Subsystems.singleMotor.setSpeed(self.power)

    def end(self):
        subsystems.team1757Subsystems.singleMotor.setSpeed(0)

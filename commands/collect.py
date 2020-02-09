from wpilib.command import Command
import subsystems

class Collect(Command):
    """
    This command will read the joystick's y axis and use that value to control
    the speed of the turret subsystem.
    """

    def __init__(self):
        Command.__init__(self, "Follow Joystick")

        self.requires(subsystems.team1757Subsystems.ballCollector)

    def execute(self):
        subsystems.team1757Subsystems.ballCollector.setSpeed(self.getRobot().oi.joystick.getX())

    def isFinished(self):
        return False
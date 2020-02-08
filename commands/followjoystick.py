from wpilib.command import Command


class FollowJoystick(Command):
    """
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    """

    def __init__(self):
        Command.__init__(self, "Follow Joystick")

        self.requires(self.getRobot().motor)

    def execute(self):
        self.getRobot().motor.setSpeed(self.getRobot().oi.joystick.getY())

    def isFinished(self):
        return False

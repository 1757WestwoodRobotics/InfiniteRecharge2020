from wpilib import Joystick
from wpilib.command import JoystickButton

from commands.example import Example

class OI:
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.joystick = Joystick(0)
        self.trigger = JoystickButton(self.joystick, 1)
        self.trigger.whenPressed(Example())

    def getJoystick(self):
        """
        Assign commands to button actions, and publish your joysticks so you
        can read values from them later.
        """
        return self.joystick

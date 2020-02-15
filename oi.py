import wpilib
from wpilib import SmartDashboard
from wpilib import Joystick
from wpilib import XboxController
from wpilib.command import JoystickButton

import commands.rotate_turret

class OI:
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.xboxController = XboxController(1)
        self.joystick = Joystick(0)
        self.trigger = JoystickButton(self.joystick, 2)
        self.trigger.whileHeld(commands.rotate_turret.RotateTurret(active=True))

        SmartDashboard.putNumber("turret_kp", 20)
        SmartDashboard.putNumber("turret_ki", 0)
        SmartDashboard.putNumber("turret_kd", 0)
        SmartDashboard.putNumber("turret_tolerance", 0)
        SmartDashboard.putNumber("turret_target_position", 0)

    def getJoystick(self):
        """
        Assign commands to button actions, and publish your joysticks so you
        can read values from them later.
        """
        return self.joystick

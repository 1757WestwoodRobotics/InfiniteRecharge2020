import wpilib
from wpilib import SmartDashboard
from wpilib import Joystick
from wpilib import XboxController
from wpilib.command import JoystickButton

# Team 1757 stuff
import commands.rotate_turret_by_angle
import commands.rotate_turret_to_angle
import commands.rotate_control_panel
from robotmap import ColorPanelConst


class OI:
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.xboxController = XboxController(0)
        self.leftStick = Joystick(1)
        self.rightStick = Joystick(2)

        # Turret
        self.trigger = JoystickButton(self.xboxController, 2)
        self.toTrigger = JoystickButton(self.xboxController, 3)
        self.trigger.whenPressed(commands.rotate_turret_by_angle.RotateTurretByAngle(active=True))
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_kp, 0.015)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_ki, 0)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_kd, 0)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_integrator_min, -0.015)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_integrator_max,  0.015)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_tolerance, 0)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_target_position, 0)
        self.toTrigger.whenPressed(commands.rotate_turret_to_angle.RotateTurretToAngle(active=True))
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_kp, 0.015)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_ki, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_kd, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_integrator_min, -0.015)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_integrator_max,  0.015)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_tolerance, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_target_position, 0)

        # Control Panel
        self.controlPanelTrigger = JoystickButton(self.leftStick, 3)
        self.controlPanelTrigger.whileHeld(commands.rotate_control_panel.RotateControlPanel(active=True))
        SmartDashboard.setFlags(commands.rotate_control_panel.RotateControlPanel.DashboardControlPanelTargetColorKey, ColorPanelConst.PanelColors.Red)


    def getJoystick(self):
        """
        Assign commands to button actions, and publish your joysticks so you
        can read values from them later.
        """
        return self.xboxController

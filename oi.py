import wpilib
from wpilib import SmartDashboard
from wpilib import Joystick
from wpilib import XboxController
from wpilib.command import JoystickButton
from wpilib import DoubleSolenoid

# Team 1757 stuff
import commands.rotate_turret_by_angle
import commands.rotate_turret_to_angle
import commands.rotate_turret_vision
import commands.rotate_control_panel
from commands.stop_compress import StopCompress
from commands.set_solenoid import SetSolenoid
from commands.set_solenoid_loop import SetSolenoidLoop
from commands.raise_lift import RaiseLift
from commands.lower_lift import LowerLift

from robotmap import ColorPanelConst, xboxButtons
import subsystems


class OI:
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.xboxController = XboxController(0)
        self.leftStick = Joystick(1)
        self.rightStick = Joystick(2)

        #Pneumatics
        JoystickButton(self.xboxController, xboxButtons.A).toggleWhenPressed(StopCompress())
        JoystickButton(self.xboxController, xboxButtons.Start).toggleWhenPressed(
            SetSolenoidLoop(subsystems.team1757Subsystems.pneumatics.discbrake))

        # lift
        self.raiselift = JoystickButton(self.xboxController, xboxButtons.RB)
        self.lowerlift = JoystickButton(self.xboxController, xboxButtons.LB)
        self.raiselift.whileHeld(RaiseLift(.5))
        self.lowerlift.whileHeld(LowerLift(.5))
    
        # Turret
        self.trigger = JoystickButton(self.xboxController, xboxButtons.B)
        self.toTrigger = JoystickButton(self.xboxController, xboxButtons.X)
        self.visionTrigger = JoystickButton(self.xboxController, xboxButtons.Y)
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
        self.visionTrigger.whileHeld(commands.rotate_turret_vision.RotateTurretVision(active=True))
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_kp, 0.015)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_ki, 0)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_kd, 0)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_integrator_min, -0.015)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_integrator_max,  0.015)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_tolerance, 0)

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

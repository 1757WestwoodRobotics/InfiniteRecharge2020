import wpilib
from wpilib import SmartDashboard
from wpilib import Joystick
from wpilib import XboxController
from wpilib.command import JoystickButton
from wpilib import DoubleSolenoid

# Team 1757 stuff
import subsystems
from robotmap import ColorPanelConst, xboxButtons, xboxAxes
import commands.rotate_turret_by_angle
import commands.rotate_turret_to_angle
import commands.rotate_turret_vision
import commands.rotate_control_panel
from commands.stop_compress import StopCompress
from commands.set_solenoid import SetSolenoid
from commands.set_solenoid_loop import SetSolenoidLoop
from commands.set_double_solenoid import SetDoubleSolenoid
from commands.set_double_solenoid_loop import SetDoubleSolenoidLoop
from commands.raise_lift import RaiseLift
from commands.lower_lift import LowerLift
from commands.brake import Brake
from commands.test import Test

class OI:
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        
        ''' Joysticks:
        xboxController is main Xbox Controller
        left and right stick are the two flight sticks
        xboxController2 is for testing commands in oi, to avoid overwriting the actual driver commands
        '''
        self.xboxController = XboxController(0)
        self.leftStick = Joystick(1)
        self.rightStick = Joystick(2)
        
        self.controlSystem = Joystick(3)
        self.xboxController2 = XboxController(4)

        #---Xbox Controller---#

        #Drivetrain
        JoystickButton(self.xboxController, xboxButtons.LB).whileHeld(Brake())

        #Lift
        JoystickButton(self.xboxController, xboxButtons.Y).whileHeld(RaiseLift(.5))
        JoystickButton(self.xboxController, xboxButtons.A).whileHeld(LowerLift(.5))
        JoystickButton(self.xboxController, xboxButtons.B).whenPressed(
            SetDoubleSolenoid(subsystems.team1757Subsystems.lift.discBrake, DoubleSolenoid.Value.kForward))
        JoystickButton(self.xboxController, xboxButtons.Back).whenPressed(
            SetDoubleSolenoid(subsystems.team1757Subsystems.lift.discBrake, DoubleSolenoid.Value.kReverse))
        
        #Pneumatics
        JoystickButton(self.xboxController2, xboxButtons.A).toggleWhenPressed(StopCompress())
        JoystickButton(self.xboxController2, xboxButtons.Start).toggleWhenPressed(
            SetDoubleSolenoidLoop(subsystems.team1757Subsystems.controlPanel.controlPanel))
    
        #Turret
        self.trigger = JoystickButton(self.xboxController2, xboxButtons.B)
        self.toTrigger = JoystickButton(self.xboxController2, xboxButtons.X)
        self.visionTrigger = JoystickButton(self.xboxController2, xboxButtons.Y)
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

        #Control Panel
        self.controlPanelTrigger = JoystickButton(self.leftStick, 3)
        self.controlPanelTrigger.whileHeld(commands.rotate_control_panel.RotateControlPanel(active=True))
        SmartDashboard.setFlags(commands.rotate_control_panel.RotateControlPanel.DashboardControlPanelTargetColorKey, ColorPanelConst.PanelColors.Red)


    def getJoystick(self):
        """
        Assign commands to button actions, and publish your joysticks so you
        can read values from them later.
        """
        return self.xboxController2

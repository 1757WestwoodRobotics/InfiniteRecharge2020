import wpilib
from wpilib import SmartDashboard
from wpilib import Joystick
from wpilib import XboxController
from wpilib.command import JoystickButton

# Team 1757 stuff
import subsystems
from robotmap import ColorPanelConst, xboxButtons, xboxAxes, ControlSystem
import commands.rotate_turret_by_angle
import commands.rotate_turret_to_angle
import commands.rotate_turret_vision
from commands.raise_lift import RaiseLift
from commands.lower_lift import LowerLift
from commands.brake import Brake
from commands.test import Test
from commands.spin_ball_loader import SpinBallLoader
from commands.shooter_spin import ShooterSpin
from commands.rotate_turret_vision import RotateTurretVision
from commands.rotate_turret_by_angle import RotateTurretByAngle
from commands.rotate_turret_to_angle import RotateTurretToAngle

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

        
        # |---Xbox Controller---|

        #Drivetrain
        JoystickButton(self.xboxController, xboxButtons.LB).whileHeld(Brake())

        #Lift
        JoystickButton(self.xboxController, xboxButtons.Y).whileHeld(RaiseLift(.5))
        JoystickButton(self.xboxController, xboxButtons.A).whileHeld(LowerLift(.5))
        
        # |---Control System---|

        #Ball Loader
        JoystickButton(self.controlSystem, ControlSystem.Button2).whileHeld(
            SpinBallLoader(.75, .5))
        JoystickButton(self.controlSystem, ControlSystem.Button3).whileHeld(
            SpinBallLoader(-.75, -.25))

        #Shooter
        JoystickButton(self.controlSystem, ControlSystem.Switch5).whileHeld(
            ShooterSpin())

        #Turret
        JoystickButton(self.controlSystem, ControlSystem.Switch3).whileHeld(RotateTurretVision())
        JoystickButton(self.controlSystem, ControlSystem.Button4).whenPressed(RotateTurretByAngle())
        JoystickButton(self.controlSystem, ControlSystem.Button5).whenPressed(RotateTurretToAngle())


        # |---Xbox Controller 2---|

        #Ball Loader
        JoystickButton(self.controlSystem, xboxButtons.A).whileHeld(
            SpinBallLoader(.75, .5))
        JoystickButton(self.controlSystem, xboxButtons.B).whileHeld(
            SpinBallLoader(-.75, -.25))

        #Shooter
        JoystickButton(self.xboxController2, xboxButtons.Y).toggleWhenPressed(ShooterSpin())


        #|---Smart Dashboard---|
        #Shooter
        SmartDashboard.putBoolean("Shooter Spinning", subsystems.team1757Subsystems.shooter.spinning)

        #Turret
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_kp, 0.015)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_ki, 0)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_kd, 0)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_integrator_min, -0.015)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_integrator_max,  0.015)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_tolerance, 0)
        SmartDashboard.putNumber(commands.rotate_turret_by_angle.RotateTurretByAngle.dashboard_target_position, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_kp, 0.015)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_ki, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_kd, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_integrator_min, -0.015)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_integrator_max,  0.015)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_tolerance, 0)
        SmartDashboard.putNumber(commands.rotate_turret_to_angle.RotateTurretToAngle.dashboard_target_position, 0)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_kp, 0.015)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_ki, 0)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_kd, 0)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_integrator_min, -0.015)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_integrator_max,  0.015)
        SmartDashboard.putNumber(commands.rotate_turret_vision.RotateTurretVision.dashboard_tolerance, 0)


    def getJoystick(self):
        """
        Assign commands to button actions, and publish your joysticks so you
        can read values from them later.
        """
        return self.xboxController

import wpilib
from wpilib import SmartDashboard
from wpilib import Joystick
from wpilib import XboxController
from wpilib.command import JoystickButton

# Team 1757 stuff
import subsystems
from robotmap import xboxButtons, ControlSystem
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
from commands.set_lift_brake import SetLiftBrake

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
        self.leftStick = Joystick(3)
        self.rightStick = Joystick(4)
        
        self.controlSystem = Joystick(1)
        self.xboxController2 = XboxController(2)

        
        # |---Xbox Controller---|

        #Drivetrain - NOTE: RT raises elevator, LT lowers elevator
        JoystickButton(self.xboxController, xboxButtons.LB).whileHeld(Brake())

        # Elevator
        JoystickButton(self.xboxController, xboxButtons.A).whileHeld(SetLiftBrake(True))
        JoystickButton(self.xboxController, xboxButtons.B).whileHeld(SetLiftBrake(False))

        
        # |---Control System---|

        #Ball Loader
        JoystickButton(self.controlSystem, ControlSystem.BottomMiddle).whileHeld(
            SpinBallLoader(.75, .5))
        JoystickButton(self.controlSystem, ControlSystem.BottomRight).whileHeld(
            SpinBallLoader(-.75, -.25))

        #Elevator
        JoystickButton(self.controlSystem, ControlSystem.TopMiddle).whileHeld(
            RaiseLift(1))
        JoystickButton(self.controlSystem, ControlSystem.TopRight).whileHeld(
            LowerLift(1))
        
        #Shooter
        JoystickButton(self.controlSystem, ControlSystem.SwitchA).whileHeld(
            ShooterSpin())

        #Turret
        JoystickButton(self.controlSystem, ControlSystem.SwitchB).whileHeld(
            RotateTurretVision())
        JoystickButton(self.controlSystem, ControlSystem.BottomLeft).whenPressed(
            RotateTurretByAngle())
        JoystickButton(self.controlSystem, ControlSystem.TopLeft).whenPressed(
            RotateTurretToAngle())


        # |---Xbox Controller 2---|

        #Ball Loader
        JoystickButton(self.controlSystem, xboxButtons.A).whileHeld(
            SpinBallLoader(.75, .5))
        JoystickButton(self.controlSystem, xboxButtons.B).whileHeld(
            SpinBallLoader(-.75, -.25))

        #Shooter
        JoystickButton(self.xboxController2, xboxButtons.Y).toggleWhenPressed(
            ShooterSpin())

        #Turret
        JoystickButton(self.xboxController2, xboxButtons.RS).whileHeld(
            RotateTurretVision())
        JoystickButton(self.xboxController2, xboxButtons.LB).whileHeld(
            RotateTurretToAngle())
        JoystickButton(self.xboxController2, xboxButtons.RB).whileHeld(
            RotateTurretByAngle())


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

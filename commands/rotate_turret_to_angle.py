import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.controller import PIDController
import subsystems

class RotateTurretToAngle(Command):
    '''inputs'''
    dashboard_kp = "rotate_turret_to_angle_kp"
    dashboard_ki = "rotate_turret_to_angle_ki"
    dashboard_kd = "rotate_turret_to_angle_kd"
    dashboard_tolerance = "rotate_turret_to_angle_tolerance"
    dashboard_integrator_min = "rotate_turret_to_angle_integrator_min"
    dashboard_integrator_max = "rotate_turret_to_angle_integrator_max"
    dashboard_target_position = "rotate_turret_to_angle_target_position"

    '''outputs'''
    dashboard_actual_position = "rotate_turret_to_angle_actual_position"
    dashboard_active = "rotate_turret_to_angle_active"
    dashboard_controller_output = "rotate_turret_to_angle_controller_output"
    dashboard_at_position = "rotate_turret_to_angle_at_position"
    dashboard_position_error = "rotate_turret_to_angle_position_error"

    """
    This command will rotate the turret to the value
    read from smartdashboard.
    """

    def __init__(self, active=False):
        Command.__init__(self, "Rotate Turret To Angle")
        self.kp_last = 0
        self.ki_last = 0
        self.kd_last = 0
        self.tolerance_last = 0
        self.controller = PIDController(0, 0, 0)
        self.integrator_min_last = 0
        self.integrator_max_last = 0
        self.active = active
        self.requires(subsystems.team1757Subsystems.turret)

    def execute(self):
        actual_position = subsystems.team1757Subsystems.turret.getPositionDegrees()
        SmartDashboard.putNumber(RotateTurretToAngle.dashboard_actual_position, actual_position)
        SmartDashboard.putBoolean(RotateTurretToAngle.dashboard_active, self.active)
        kp = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_kp, 0)
        ki = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_ki, 0)
        kd = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_kd, 0)
        integrator_min = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_integrator_min, 0)
        integrator_max = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_integrator_max, 0)
        if ((kp != self.kp_last)
            or (ki != self.ki_last)
            or (kd != self.kd_last)
            or (integrator_min != self.integrator_min_last)
            or (integrator_max != self.integrator_max_last)):
            self.controller.setP(kp)
            self.controller.setI(ki)
            self.controller.setD(kd)
            self.controller.setIntegratorRange(integrator_min, integrator_max)
            self.controller.reset()
            self.kp_last = kp
            self.ki_last = ki
            self.kd_last = kd
            self.integrator_min_last = integrator_min
            self.integrator_max_last = integrator_max
        tolerance = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_tolerance, 0)
        self.controller.setTolerance(tolerance)
        target_position = SmartDashboard.getNumber(RotateTurretToAngle.dashboard_target_position, 0)
        #lower_limit = subsystems.team1757Subsystems.turret.getLowerLimitDegrees()
        #upper_limit = subsystems.team1757Subsystems.turret.getUpperLimitDegrees()
        #target_position = min(max(target_position, lower_limit), upper_limit)
        if (self.active):
            controller_output = self.controller.calculate(actual_position, target_position)
            # if (((controller_output < 0) 
            #         and (actual_position < lower_limit))
            #     or ((controller_output > 0)
            #         and (actual_position > upper_limit))):
            #     controller_output = 0
            subsystems.team1757Subsystems.turret.setSpeed(controller_output)
            SmartDashboard.putNumber(RotateTurretToAngle.dashboard_controller_output, controller_output)
            SmartDashboard.putBoolean(RotateTurretToAngle.dashboard_at_position, self.controller.atSetpoint())
            SmartDashboard.putNumber(RotateTurretToAngle.dashboard_position_error, self.controller.getPositionError())
        else:
            subsystems.team1757Subsystems.turret.setSpeed(0)
            SmartDashboard.putNumber(RotateTurretToAngle.dashboard_controller_output, 0)
            SmartDashboard.putBoolean(RotateTurretToAngle.dashboard_at_position, False)
            SmartDashboard.putNumber(RotateTurretToAngle.dashboard_position_error, 0)

    def isFinished(self):
        return self.controller.atSetpoint()

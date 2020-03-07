import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.controller import PIDController
from networktables import NetworkTables
import subsystems

class RotateTurretVision(Command):
    """
    Command to rotate the turret by vision, to target reflective tape
    """
    
    '''inputs'''
    dashboard_kp = "rotate_turret_to_angle_kp"
    dashboard_ki = "rotate_turret_to_angle_ki"
    dashboard_kd = "rotate_turret_to_angle_kd"
    dashboard_tolerance = "rotate_turret_to_angle_tolerance"
    dashboard_integrator_min = "rotate_turret_to_angle_integrator_min"
    dashboard_integrator_max = "rotate_turret_to_angle_integrator_max"
    # dashboard_target_position = "rotate_turret_by_angle_target_position"

    '''outputs'''
    dashboard_actual_position = "rotate_turret_vision_actual_position"
    dashboard_active = "rotate_turret_vision_active"
    dashboard_controller_output = "rotate_turret_vision_controller_output"
    dashboard_at_position = "rotate_turret_vision_at_position"
    dashboard_position_error = "rotate_turret_vision_position_error"

    def __init__(self):
        Command.__init__(self, "Rotate Turret Using Vision")
        self.limelight = NetworkTables.getTable("limelight")
        self.kp_last = 0
        self.ki_last = 0
        self.kd_last = 0
        self.tolerance_last = 0
        self.controller = PIDController(0, 0, 0)
        self.integrator_min_last = 0
        self.integrator_max_last = 0
        self.requires(subsystems.team1757Subsystems.turret)
        self.isDone = False

    def execute(self):
        if self.controller.atSetpoint():
            self.isDone = False
        if self.isDone == False:
            self.original_position = subsystems.team1757Subsystems.turret.getPositionDegrees()
            self.isDone = True
        actual_position = subsystems.team1757Subsystems.turret.getPositionDegrees()
        SmartDashboard.putNumber(RotateTurretVision.dashboard_actual_position, actual_position)
        SmartDashboard.putBoolean(RotateTurretVision.dashboard_active, True)
        kp = SmartDashboard.getNumber(RotateTurretVision.dashboard_kp, 0)
        ki = SmartDashboard.getNumber(RotateTurretVision.dashboard_ki, 0)
        kd = SmartDashboard.getNumber(RotateTurretVision.dashboard_kd, 0)
        integrator_min = SmartDashboard.getNumber(RotateTurretVision.dashboard_integrator_min, 0)
        integrator_max = SmartDashboard.getNumber(RotateTurretVision.dashboard_integrator_max, 0)
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
        tolerance = SmartDashboard.getNumber(RotateTurretVision.dashboard_tolerance, 0)
        self.controller.setTolerance(tolerance)
        target_position = actual_position + self.limelight.getNumber("tx", 0) * -1 # Change actual_position to self.original_position if this no longer works
        #lower_limit = subsystems.team1757Subsystems.turret.getLowerLimitDegrees()
        #upper_limit = subsystems.team1757Subsystems.turret.getUpperLimitDegrees()
        #target_position = min(max(target_position, lower_limit), upper_limit)
        controller_output = self.controller.calculate(actual_position, target_position)
        #print(target_position)
        # if (((controller_output < 0) 
        #         and (actual_position < lower_limit))
        #     or ((controller_output > 0)
        #         and (actual_position > upper_limit))):
        #     controller_output = 0
        subsystems.team1757Subsystems.turret.setSpeed(controller_output)
        SmartDashboard.putNumber(RotateTurretVision.dashboard_controller_output, controller_output)
        SmartDashboard.putBoolean(RotateTurretVision.dashboard_at_position, self.controller.atSetpoint())
        SmartDashboard.putNumber(RotateTurretVision.dashboard_position_error, self.controller.getPositionError())

        # if subsystems.team1757Subsystems.turret.leftstatus or subsystems.team1757Subsystems.turret.rightstatus:
        #     subsystems.team1757Subsystems.turret.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.turret.setSpeed(0)
        SmartDashboard.putNumber(RotateTurretVision.dashboard_controller_output, 0)
        SmartDashboard.putBoolean(RotateTurretVision.dashboard_at_position, False)
        SmartDashboard.putNumber(RotateTurretVision.dashboard_position_error, 0)

    def isFinished(self):
        return self.controller.atSetpoint()

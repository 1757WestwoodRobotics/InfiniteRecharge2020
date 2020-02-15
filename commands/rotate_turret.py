import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.controller import PIDController
import subsystems

class RotateTurret(Command):
    """
    This command will read rotate the turret to the value
    from smartdashboard.
    """

    def __init__(self, active=False):
        Command.__init__(self, "Rotate Turret")
        self.kp_last = 0
        self.ki_last = 0
        self.kd_last = 0
        self.tolerance_last = 0
        self.controller = PIDController(0, 0, 0)
        self.active = active
        self.requires(subsystems.team1757Subsystems.turret)

    def execute(self):
        actual_position = subsystems.team1757Subsystems.turret.getPosition()
        SmartDashboard.putNumber("turret_actual_position", actual_position)
        SmartDashboard.putBoolean("turret_active", self.active)
        kp = SmartDashboard.getNumber("turret_kp", 0)
        ki = SmartDashboard.getNumber("turret_ki", 0)
        kd = SmartDashboard.getNumber("turret_kd", 0)
        if (kp != self.kp_last):
            self.controller.setP(kp)
            self.controller.reset()
            self.kp_last = kp
        if (ki != self.ki_last):
            self.controller.setI(ki)
            self.controller.reset()
            self.ki_last = ki
        if (kd != self.kd_last):
            self.controller.setD(kd)
            self.controller.reset()
            self.kd_last = kd
        tolerance = SmartDashboard.getNumber("turret_tolerance", 0)
        self.controller.setTolerance(tolerance)
        target_position = SmartDashboard.getNumber("turret_target_position", 0)
        if (self.active):
            controller_output = self.controller.calculate(actual_position, target_position)
            subsystems.team1757Subsystems.turret.setSpeed(controller_output)
            SmartDashboard.putNumber("turret_controller_output", controller_output)
            SmartDashboard.putBoolean("turret_at_position", self.controller.atSetpoint())
            SmartDashboard.putNumber("turret_position_error", self.controller.getPositionError())
        else:
            subsystems.team1757Subsystems.turret.setSpeed(0)
            SmartDashboard.putNumber("turret_controller_output", 0)
            SmartDashboard.putBoolean("turret_at_position", False)
            SmartDashboard.putNumber("turret_position_error", 0)


    def isFinished(self):
        return False

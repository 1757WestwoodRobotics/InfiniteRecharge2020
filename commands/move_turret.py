import wpilib
import subsystems
from wpilib.command import Command

class MoveTurret(Command):
    '''
    Command to move the turret

    Parameters:

    Engaged: If true, the brake will engage, if false, it will retract
    '''
    def __init__(self):
        Command.__init__(self, "Move Turret")
        wpilib.SmartDashboard.putNumber("Turret Move Speed", 0)

    def execute(self):
        speed = wpilib.SmartDashboard.getNumber("Turret Move Speed", 0)
        subsystems.team1757Subsystems.turret.setSpeed(speed)

    def end(self):
        subsystems.team1757Subsystems.turret.setSpeed(0)

    def isFinished(self):
        return False

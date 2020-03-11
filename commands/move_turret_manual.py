import wpilib
import subsystems
from wpilib.command import Command

class MoveTurretManual(Command):
    '''
    Command to move the turret manually at .1 output

    Parameters:

    Right: If true, the turret will turn right, if false, turret will turn left
    '''
    def __init__(self, right):
        Command.__init__(self, "Move Turret Manual")
        self.requires(subsystems.team1757Subsystems.turret)

        self.right = right
        self.speed = -.1 if right else .1

    def execute(self):
        subsystems.team1757Subsystems.turret.setSpeed(self.speed)
        
    def end(self):
        subsystems.team1757Subsystems.turret.setSpeed(0)

    def isFinished(self):
        return False

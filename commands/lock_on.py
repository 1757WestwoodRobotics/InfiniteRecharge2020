import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class lock_on(Command):

    def __init__(self, active=False):
        Command.__init__(self, "lock_on")

        self.requires(subsystems.team1757Subsystems.vision)

    def execute(self):
        subsystems.team1757Subsystems.vision.lock_on_target()

    # def isFinished(self):
    #     return False
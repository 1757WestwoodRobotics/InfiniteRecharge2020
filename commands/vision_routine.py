import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
from wpilib.interfaces import GenericHID
import subsystems

class VisionRoutine(Command):

    def __init__(self):
        Command.__init__(self, "VisionRoutine")

        self.requires(subsystems.team1757Subsystems.vision)

    def execute(self):
        target_information_list = []
        target_information_list = subsystems.team1757Subsystems.vision.add_target_info_to_list(target_information_list)

    def isFinished(self):
        return False
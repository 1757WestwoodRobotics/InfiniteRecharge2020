import wpilib
from wpilib.command import Command
import subsystems

class RotateControlPanelManual(Command):
    '''
    Command to manually spin the control panel wheel

    '''

    def __init__(self, speed):
        Command.__init__(self, "Rotate Control Panel Manual")

        self.requires(subsystems.team1757Subsystems.controlPanel)

        self.speed = speed

    def execute(self):
        subsystems.team1757Subsystems.controlPanel.setSpeed(self.speed)

    def isFinished(self):
        return True
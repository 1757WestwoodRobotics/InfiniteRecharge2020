import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
import subsystems

class StopCompress(Command):
    '''
    Command for compressor to stop compressing air.
    
    The default state of the compress is enabled,
    and when the command ends, the compressor is reenabled.
    '''

    def __init__(self):
        Command.__init__(self, "Stop Compress")

        self.requires(subsystems.team1757Subsystems.pneumatics)

    def execute(self):
        subsystems.team1757Subsystems.pneumatics.setCompressor(False)

    def end(self):
        subsystems.team1757Subsystems.pneumatics.setCompressor(True)

    def isFinished(self):
        return False
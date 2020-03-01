import wpilib
from wpilib.command import Command
import subsystems

class SpinBallLoader(Command):
    '''
    Command to spin the wheels of the ball loader

    Lower motor at 75%, upper motor at 50% output
    '''

    def __init__(self):
        Command.__init__(self, "Spin Ball Loader")
        self.requires(subsystems.team1757Subsystems.ballLoader)

    def execute(self):
        subsystems.team1757Subsystems.ballLoader.spin(.75, .5)

    def end(self):
        subsystems.team1757Subsystems.ballLoader.stopSpin()

    def isFinished(self):
        return True
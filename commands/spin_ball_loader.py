import wpilib
from wpilib.command import Command
import subsystems

class SpinBallLoader(Command):
    '''
    Command to spin the wheels of the ball loader

    Parameters:

    Speed: Speed of the motors from -1 to 1
    '''

    def __init__(self, speed):
        Command.__init__(self, "Spin Ball Loader")
        self.requires(subsystems.team1757Subsystems.ballLoader)
        
        self.speed = speed

    def execute(self):
        subsystems.team1757Subsystems.ballLoader.spin(self.speed)

    def end(self):
        subsystems.team1757Subsystems.ballLoader.stopSpin()

    def isFinished(self):
        return True
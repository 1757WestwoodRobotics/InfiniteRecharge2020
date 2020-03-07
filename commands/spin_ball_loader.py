import wpilib
from wpilib.command import Command
import subsystems

class SpinBallLoader(Command):
    '''
    Command to spin the wheels of the ball loader

    Parameters:
    
    Lower Speed: Speed of the lower motor from -1 to 1

    Upper Speed: Speed of the upper motor from -1 to 1
    '''

    def __init__(self, lowerSpeed, upperSpeed):
        Command.__init__(self, "Spin Ball Loader")
        self.requires(subsystems.team1757Subsystems.ballLoader)
        
        self.lowerSpeed = lowerSpeed
        self.upperSpeed = upperSpeed

    def execute(self):
        subsystems.team1757Subsystems.ballLoader.spin(self.lowerSpeed, self.upperSpeed)

    def end(self):
        subsystems.team1757Subsystems.ballLoader.stopSpin()

    def isFinished(self):
        return False
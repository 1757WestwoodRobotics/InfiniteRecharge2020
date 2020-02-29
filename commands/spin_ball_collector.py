import wpilib
from wpilib.command import Command
import subsystems

class SpinBallCollector(Command):
    '''
    Command to spin the wheels of the ball collector
    '''

    def __init__(self, speed):
        Command.__init__(self, "Spin Ball Collector")
        self.requires(subsystems.team1757Subsystems.ballCollector)

        self.speed = speed

    def execute(self):

        self.RT = (self.getRobot().oi.xboxController.getRawAxis(3))
        self.LT = (self.getRobot().oi.xboxController.getRawAxis(2))

        if self.RT > .75:
            self.spinSpeed = self.speed
        elif self.LT > .75:
            self.spinSpeed = -self.speed
        else:
            self.spinSpeed = 0

        subsystems.team1757Subsystems.ballCollector.spin(self.spinSpeed)

    def isFinished(self):
        return True
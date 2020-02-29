from wpilib.command import Command
import subsystems

class SpinUp(Command):

    def __init__(self):
        Command.__init__(self, "Spin Shooter")
        self.requires(subsystems.team1757Subsystems.shooter)

    def execute(self):
        subsystems.team1757Subsystems.shooter.spinUp()
    
    def end(self):
        subsystems.team1757Subsystems.shooter.spinDown()

    def isFinished(self):
        return False
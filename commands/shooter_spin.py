from wpilib.command import Command
import subsystems

class ShooterSpin(Command):
    '''
    Command to spin the wheels of the shooter
    
    While the command is executing, the wheels are spinning at veloicty, when the command ends, the wheels stop spinning
    '''
    def __init__(self):
        Command.__init__(self, "Shooter Spin")
        self.requires(subsystems.team1757Subsystems.shooter)

    def execute(self):
        subsystems.team1757Subsystems.shooter.spinning = True
        subsystems.team1757Subsystems.shooter.spinUp()
    
    def end(self):
        subsystems.team1757Subsystems.shooter.spinning = False
        subsystems.team1757Subsystems.shooter.spinDown()

    def isFinished(self):
        return False
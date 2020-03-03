import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class LowerLift(Command):

    def __init__(self):
        Command.__init__(self, "LowerLift")

        self.requires(subsystems.team1757Subsystems.lift)
    # need pneumatic subsystem bc of discbrake
    # disengage brake

    def execute(self):

        self.LT = (self.getRobot().oi.xboxController.getRawAxis(2))

        subsystems.team1757Subsystems.lift.setSpeed(-self.LT)
            
        if subsystems.team1757Subsystems.lift.revstatus:
            subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

    def isFinished(self):
        return False
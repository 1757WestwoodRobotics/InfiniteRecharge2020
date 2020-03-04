import wpilib
from wpilib.command import Command
import subsystems
from ctre import WPI_TalonSRX
from robotmap import Can

class MoveLift(Command):
    '''
    Command to move the elevator up or down

    Right Trigger raises the elevator

    Left Trigger lowers the elevator

    Default command of the lift subsystem
    '''
    def __init__(self):
        Command.__init__(self, "Move Lift")

        self.requires(subsystems.team1757Subsystems.lift)
    # need pneumatic subsystem bc of discbrake
    # disengage brake

    def execute(self):

        self.RT = (self.getRobot().oi.xboxController.getRawAxis(3))
        self.LT = (self.getRobot().oi.xboxController.getRawAxis(2))
        
        if self.RT > self.LT:
            subsystems.team1757Subsystems.lift.setSpeed(self.RT)
        else:
            subsystems.team1757Subsystems.lift.setSpeed(-self.LT)

        # if subsystems.team1757Subsystems.lift.fwdstatus:
        #     subsystems.team1757Subsystems.lift.setSpeed(0)

    def end(self):
        subsystems.team1757Subsystems.lift.setSpeed(0)

# ^ is this enough to keep motors from turning at all costs?

    def isFinished(self):
        return False

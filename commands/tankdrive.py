import wpilib
from wpilib.command import Command
import subsystems

class TankDrive(Command):
    '''
    Command to drive robot using two-joystick tank drive
    '''

    def __init__(self):
        Command.__init__(self, "TankDrive")

        self.requires(subsystems.team1757Subsystems.drivetrain)

    def execute(self):
        self.leftSpeed = -self.getRobot().oi.leftStick.getY()
        self.rightSpeed = -self.getRobot().oi.rightStick.getY()

        subsystems.team1757Subsystems.drivetrain.tankDrive(self.leftSpeed, self.rightSpeed, True)

    def isFinished(self):
        return False
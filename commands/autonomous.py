from wpilib.command import CommandGroup

from wpilib.command import WaitCommand
from commands.driveforward import DriveForward


class AutonomousProgram(CommandGroup):
    """
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    """

    def __init__(self):
        CommandGroup.__init__(self, "Autonomous Program")
        print("Autonomous initiated")
        self.addSequential(DriveForward(5, .5))
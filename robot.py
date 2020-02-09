#!/usr/bin/env python3

import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot

from subsystems import singlemotor, drivetrain
import oi
from commands.autonomous import AutonomousProgram


class Robot(CommandBasedRobot):
    """
    The CommandBasedRobot base class implements almost everything you need for
    a working robot program. All you need to do is set up the subsystems and
    commands. You do not need to override the "periodic" functions, as they
    will automatically call the scheduler. You may override the "init" functions
    if you want to do anything special when the mode changes.
    """

    def robotInit(self):
        """
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        """

        ###### Singleton magic - ignore for now
        Command.getRobot = lambda x=0: self
        ###### Stop ignoring ##################

        self.motor = singlemotor.SingleMotor()

        self.drivetrain = drivetrain.Drivetrain()

        self.autonomousProgram = AutonomousProgram()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        self.oi = oi.OI(self)

    def autonomousInit(self):
        """
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        """

        self.autonomousProgram.start()


if __name__ == "__main__":
    wpilib.run(Robot)

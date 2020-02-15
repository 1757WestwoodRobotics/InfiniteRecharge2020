#!/usr/bin/env python3

import wpilib
from wpilib.command import Command
from wpilib.command import Scheduler
from commandbased import CommandBasedRobot

# Team 1757 stuff
import oi
# subsystems
import subsystems.team1757Subsystems
# commands
import commands.autonomous

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
        Creates the robot singleton
        """
        Command.getRobot = lambda x=0: self

        """
        Subsystems are instantiated in the global init
        """
        subsystems.team1757Subsystems.init()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        self.oi = oi.OI(self)

        """
        Commands used directly by the robot program 
        All other commands are instatiated in OI
        """
        self.autonomousProgram = commands.autonomous.AutonomousProgram()

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

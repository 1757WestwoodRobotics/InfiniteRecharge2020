# Westwood FRC Team 1757
# 2020

# Command to rotate control panel to desired color

import wpilib
from wpilib import SmartDashboard
from wpilib.command import Command
import subsystems
from subsystems import controlpanel


class RotateControlPanel(Command):
    '''inputs'''
    DashboardControlPanelTargetColorKey = "Control Panel Target Color"

    '''outputs'''
    DashboardControlPanelCurrentColorKey = "Control Panel Current Color"


    def __init__(self, active=False):
        Command.__init__(self, "RotateControlPanel")
        self.requires(subsystems.team1757Subsystems.gControlPanel)
        self.__controlPanelSystem = subsystems.team1757Subsystems.gControlPanel


    def initialize(self):
        self.__controlPanelSystem.setTargetColor(self.getTargetControlPanelColor())


    # Central location where we get the target control panel color.
    # Change this function to get it from dashboard, button click, the field, or wherever.
    def getTargetControlPanelColor(self):
        return SmartDashboard.getFlags(RotateControlPanel.DashboardControlPanelTargetColorKey)



    def execute(self):
        currentPanelColor = self.__controlPanelSystem.currentPanelColor()
        SmartDashboard.putNumber(RotateControlPanel.DashboardControlPanelCurrentColorKey, currentPanelColor)
        if (self.active):
            self.__controlPanelSystem.seek()

    def isFinished(self):
        return self.__controlPanelSystem.found()

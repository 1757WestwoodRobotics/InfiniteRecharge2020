# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the control panel color detection algorithm
# that is buried in subsystems.controlpanel.py

import wpilib
from wpilib import SmartDashboard
from wpilib import Timer
from wpilib.command import Command
import subsystems
import time

class TestControlPanelColor2(Command):
    '''outputs'''
    dashboard_color_sensor_detected_color = "read_color_detected_color"
    

    def __init__(self):
        Command.__init__(self)
        self.requires(subsystems.team1757Subsystems.controlPanel)


    def execute(self):

        controlPanelSystem = subsystems.team1757Subsystems.controlPanel
        controlPanelSystem.updatePanelColor()
        currentColor = controlPanelSystem.currentPanelColor
        print(currentColor)
        SmartDashboard.putNumber(TestControlPanelColor2.dashboard_color_sensor_detected_color, currentColor)


    def isFinished(self):
        return False

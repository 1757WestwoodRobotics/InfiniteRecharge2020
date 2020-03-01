# Westwood FRC Team 1757
# 2020

# Simple Command class for working out the control panel color detection algorithm.
# This algorithm has been re-factored and pushed down into the controlpanel subsystem,
# so this command should be retired in favor of TestControlPanelColor2, which is a
# Command class that uses the controlpanel subsystem.

import wpilib
from wpilib import SmartDashboard
from wpilib import Timer
from wpilib.command import Command
import subsystems
import time

class TestControlPanelColor(Command):
    '''outputs'''
    dashboard_color_sensor_ir = "read_color_sensor_ir"
    dashboard_color_sensor_red = "read_color_sensor_red"
    dashboard_color_sensor_green = "read_color_sensor_green"
    dashboard_color_sensor_blue = "read_color_sensor_blue"
    dashboard_color_sensor_proximity = "read_color_sensor_proximity"
    dashboard_color_sensor_detected_color = "read_color_detected_color"
    dashboard_color_sensor_loops = "read_color_loops"
    dashboard_color_sensor_distance_from_point_to_redRef = "read_color_distance_from_point_to_redRef"
    dashboard_color_sensor_distance_from_point_to_greenRef = "read_color_distance_from_point_to_greenRef"
    dashboard_color_sensor_distance_from_point_to_blueRef = "read_color_distance_from_point_to_blueRef"
    dashboard_color_sensor_distance_from_point_to_yellowRef = "read_color_distance_from_point_to_yellowRef"
    
    #red
    redRef = [0.512329,0.348755,0.139038] #Coordinate values that DO NOT CHANGE

    #green
    greenRef = [0.168579,0.574585,0.256958] #Coordinate values that DO NOT CHANGE

    #blue
    blueRef = [0.127319,0.423462,0.449097] #Coordinate values that DO NOT CHANGE

    #yellow
    yellowRef = [0.316284,0.556763,0.126831] #Coordinate values that DO NOT CHANGE  

    #distance from yellow to green
    yg_distance = (yellowRef[0] - greenRef[0])**2 + (yellowRef[1] - greenRef[1])**2 + (yellowRef[2] - greenRef[2])**2

    color_prev = 5
    color_count = 0
    color_out = 5

    # 0 = red, 1 = green, 2 = blue, 3 = yellow, 4 = garbage
    colors = [0, 1, 2, 3]

    # the next expected color, if not what it's supposed to be, the result is garbage
    #color_expected = 5

    # 1 is clockwise, -1 is counterclockwise
    #rotation =  1
    #loops = 0

    def __init__(self):
        Command.__init__(self)
        self.requires(subsystems.team1757Subsystems.gREVColorSensor)
        # COMMENT OUT LINE ABOVE, AND UNCOMMENT LINE BELOW TO TEST CONTROL PANEL
        #self.requires(subsystems.team1757Subsystems.gControlPanel)
        #self.color_timer = Timer()

    def execute(self):
        '''
        #timer stuff
        self.color_timer.reset()
        self.color_timer.start()'''

        threshold = 3

        theSensor = subsystems.team1757Subsystems.gREVColorSensor
        # Get the sensor attributes
        color = theSensor.color
        ir = theSensor.ir

        # Get the individual components of the color
        red = color.red
        blue = color.blue
        green = color.green

        # Get the approximate proximity of an object
        proximity = theSensor.proximity
        '''
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_ir, ir)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_red, red)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_green, green)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_blue, blue)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_proximity, proximity)
        '''
        distance_to_redRef = (red - TestControlPanelColor.redRef[0])**2 + (green - TestControlPanelColor.redRef[1])**2 + (blue - TestControlPanelColor.redRef[2])**2
        minDist = distance_to_redRef
        color = 0
        '''color_expected_index = (color + TestControlPanelColor.rotation) % len(TestControlPanelColor.colors)
        color_expected = TestControlPanelColor.colors[color_expected_index]'''
        

        distance_to_greenRef = (red - TestControlPanelColor.greenRef[0])**2 + (green - TestControlPanelColor.greenRef[1])**2 + (blue - TestControlPanelColor.greenRef[2])**2
        if ( distance_to_greenRef < minDist ):
            minDist = distance_to_greenRef
            color = 1
            # color_expected_index = (color + TestControlPanelColor.rotation) % len(TestControlPanelColor.colors)
            # color_expected = TestControlPanelColor.colors[color_expected_index]
        

        distance_to_blueRef = (red - TestControlPanelColor.blueRef[0])**2 + (green - TestControlPanelColor.blueRef[1])**2 + (blue - TestControlPanelColor.blueRef[2])**2
        if ( distance_to_blueRef < minDist ):
            minDist = distance_to_blueRef
            color = 2
            #color_expected_index = (color + TestControlPanelColor.rotation) % len(TestControlPanelColor.colors)
            #color_expected = TestControlPanelColor.colors[color_expected_index]
        

        distance_to_yellowRef = (red - TestControlPanelColor.yellowRef[0])**2 + (green - TestControlPanelColor.yellowRef[1])**2 + (blue - TestControlPanelColor.yellowRef[2])**2
        if ( distance_to_yellowRef < minDist ):
            minDist = distance_to_yellowRef
            color = 3
            # color_expected_index = (color + TestControlPanelColor.rotation) % len(TestControlPanelColor.colors)
            #color_expected = TestControlPanelColor.colors[color_expected_index]
        


        if (minDist >= 0.03*(TestControlPanelColor.yg_distance)):
            SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_detected_color, color)
            color = 4

        if (color == TestControlPanelColor.color_prev):
            TestControlPanelColor.color_count += 1
            TestControlPanelColor.color_prev = color
            
        else:
            TestControlPanelColor.color_count = 0
            TestControlPanelColor.color_prev = 5
            TestControlPanelColor.color_prev = color
        
        if (color == 4):
                threshold = 10
        else:
            threshold = 3

        if ((TestControlPanelColor.color_count >= threshold) and TestControlPanelColor.color_prev != TestControlPanelColor.color_out):
            SmartDashboard.putNumber("TestControlPanelColor.dashboard_color_sensor_detected_color", color)
            TestControlPanelColor.color_out = color
            print(color)
            '''if (TestControlPanelColor.color_expected == color):
                #TestControlPanelColor.loops += .125
            #print(color)'''
        #else:
            #TestControlPanelColor.loops = 0
            #color_expected = 
            

        #more timer stuff
        ''''self.color_timer.stop()
        time = self.color_timer.get()
        print(time)
        print(color)
        print(color_expected)'''

        #outputs
        # SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_loops, TestControlPanelColor.loops)
        '''SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_distance_from_point_to_redRef, distance_to_redRef)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_distance_from_point_to_greenRef, distance_to_greenRef)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_distance_from_point_to_blueRef, distance_to_blueRef)
        SmartDashboard.putNumber(TestControlPanelColor.dashboard_color_sensor_distance_from_point_to_yellowRef, distance_to_yellowRef)
        '''
        
        # COMMENT EVERYTHING ELSE OUT IN THIS METHOD, AND UNCOMMENT THE FOLLOWING FOUR LINES
        # TO TEST THE SAME LOGIC IMPLEMENTED IN THE CONTROL PANEL SUBSYSTEM.
        # SEE ALSO __init__() METHOD
        #controlPanelSystem = subsystems.team1757Subsystems.gControlPanel
        #controlPanelSystem.updatePanelColor()
        #currentColor = controlPanelSystem.currentPanelColor
        #print(currentColor)
        #SmartDashboard.putNumber("TestControlPanelColor.dashboard_color_sensor_detected_color", currentColor)





    def isFinished(self):
        return False

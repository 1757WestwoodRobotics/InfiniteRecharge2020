# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the REV Robotics ColorSensorV3

import wpilib
from wpilib import SmartDashboard
from wpilib import Timer
from wpilib.command import Command
import subsystems
import time

class Team1757TestColorSensorCommand(Command):
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
    rotation =  1
    loops = 0

    def __init__(self):
        Command.__init__(self)
        self.requires(subsystems.team1757Subsystems.gREVColorSensor)
        self.color_timer = Timer()

    def execute(self):

        #timer stuff
        self.color_timer.reset()
        self.color_timer.start()

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
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_ir, ir)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_red, red)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_green, green)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_blue, blue)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_proximity, proximity)
        '''
        distance_to_redRef = (red - Team1757TestColorSensorCommand.redRef[0])**2 + (green - Team1757TestColorSensorCommand.redRef[1])**2 + (blue - Team1757TestColorSensorCommand.redRef[2])**2
        minDist = distance_to_redRef
        color = 0
        color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
        color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        

        distance_to_greenRef = (red - Team1757TestColorSensorCommand.greenRef[0])**2 + (green - Team1757TestColorSensorCommand.greenRef[1])**2 + (blue - Team1757TestColorSensorCommand.greenRef[2])**2
        if ( distance_to_greenRef < minDist ):
            minDist = distance_to_greenRef
            color = 1
            color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
            color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        

        distance_to_blueRef = (red - Team1757TestColorSensorCommand.blueRef[0])**2 + (green - Team1757TestColorSensorCommand.blueRef[1])**2 + (blue - Team1757TestColorSensorCommand.blueRef[2])**2
        if ( distance_to_blueRef < minDist ):
            minDist = distance_to_blueRef
            color = 2
            color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
            color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        

        distance_to_yellowRef = (red - Team1757TestColorSensorCommand.yellowRef[0])**2 + (green - Team1757TestColorSensorCommand.yellowRef[1])**2 + (blue - Team1757TestColorSensorCommand.yellowRef[2])**2
        if ( distance_to_yellowRef < minDist ):
            minDist = distance_to_yellowRef
            color = 3
            color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
            color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        


        if (minDist >= 0.03*(Team1757TestColorSensorCommand.yg_distance)):
            #SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_detected_color, color)
            color = 4

        if (color == Team1757TestColorSensorCommand.color_prev):
            Team1757TestColorSensorCommand.color_count += 1
            Team1757TestColorSensorCommand.color_prev = color
            
        else:
            Team1757TestColorSensorCommand.color_count = 0
            Team1757TestColorSensorCommand.color_prev = 5
            Team1757TestColorSensorCommand.color_prev = color
        
        if (color == 4):
                threshold = 10
        else:
            threshold = 3

        if ((Team1757TestColorSensorCommand.color_count >= threshold) and Team1757TestColorSensorCommand.color_prev != Team1757TestColorSensorCommand.color_out):
            SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_detected_color, color)
            Team1757TestColorSensorCommand.color_out = color
            if (Team1757TestColorSensorCommand.color_expected == color):
                Team1757TestColorSensorCommand.loops += .125
            #print(color)
        else:
            #Team1757TestColorSensorCommand.loops = 0
            color_expected = 
        
        #more timer stuff
        self.color_timer.stop()
        time = self.color_timer.get()
        print(time)
        print(color)
        print(color_expected)

        #outputs
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_loops, Team1757TestColorSensorCommand.loops)
        '''SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_distance_from_point_to_redRef, distance_to_redRef)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_distance_from_point_to_greenRef, distance_to_greenRef)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_distance_from_point_to_blueRef, distance_to_blueRef)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_distance_from_point_to_yellowRef, distance_to_yellowRef)
        '''
        





    def isFinished(self):
        return False

# Westwood FRC Team 1757
# 2020

# Simple Command class for testing the REV Robotics ColorSensorV3
#
# ATTENTION!!!!
# THIS IS *TEST* CODE!  DO *NOT* DO DEVELOPMENT IN THIS FILE!
# IT SHOULD ONLY BE USED FOR BASIC SANITY CHECKS ON THE COLOR SENSOR ITSELF,
# PLUS WE WILL NEED IT TO CALIBRATE CONTROL PANEL REFERENCE COLORS ON 
# COMPETITION DAY.
#
# Thank you.


import wpilib
from wpilib.command import Command
import subsystems

class Team1757TestColorSensorCommand(Command):

    def __init__(self):
        Command.__init__(self)

        self.requires(subsystems.team1757Subsystems.gREVColorSensor)
        

    def execute(self):
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
        '''
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_red, red)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_green, green)
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_blue, blue)
        '''
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_proximity, proximity)
        '''
        distance_to_redRef = (red - Team1757TestColorSensorCommand.redRef[0])**2 + (green - Team1757TestColorSensorCommand.redRef[1])**2 + (blue - Team1757TestColorSensorCommand.redRef[2])**2
        minDist = distance_to_redRef
        color = 0
        # color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
        # color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]'''
        

        distance_to_greenRef = (red - Team1757TestColorSensorCommand.greenRef[0])**2 + (green - Team1757TestColorSensorCommand.greenRef[1])**2 + (blue - Team1757TestColorSensorCommand.greenRef[2])**2
        if ( distance_to_greenRef < minDist ):
            minDist = distance_to_greenRef
            color = 1
            # color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
            # color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        

        distance_to_blueRef = (red - Team1757TestColorSensorCommand.blueRef[0])**2 + (green - Team1757TestColorSensorCommand.blueRef[1])**2 + (blue - Team1757TestColorSensorCommand.blueRef[2])**2
        if ( distance_to_blueRef < minDist ):
            minDist = distance_to_blueRef
            color = 2
            #color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
            #color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        

        distance_to_yellowRef = (red - Team1757TestColorSensorCommand.yellowRef[0])**2 + (green - Team1757TestColorSensorCommand.yellowRef[1])**2 + (blue - Team1757TestColorSensorCommand.yellowRef[2])**2
        if ( distance_to_yellowRef < minDist ):
            minDist = distance_to_yellowRef
            color = 3
            # color_expected_index = (color + Team1757TestColorSensorCommand.rotation) % len(Team1757TestColorSensorCommand.colors)
            #color_expected = Team1757TestColorSensorCommand.colors[color_expected_index]
        


        if (minDist >= 0.03*(Team1757TestColorSensorCommand.yg_distance)):
            SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_detected_color, color)
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
            #SmartDashboard.putNumber("Team1757TestColorSensorCommand.dashboard_color_sensor_detected_color", color)
            Team1757TestColorSensorCommand.color_out = color
            print(color)
        print(color)
        
        #more timer stuff
        ''''self.color_timer.stop()
        time = self.color_timer.get()
        print(time)
        print(color)
        print(color_expected)'''

        #outputs
        SmartDashboard.putNumber("Team1757TestColorSensorCommand.dashboard_color_sensor_red", red)
        SmartDashboard.putNumber("Team1757TestColorSensorCommand.dashboard_color_sensor_green", green)
        SmartDashboard.putNumber("Team1757TestColorSensorCommand.dashboard_color_sensor_blue", blue)
        '''
        SmartDashboard.putNumber(Team1757TestColorSensorCommand.dashboard_color_sensor_distance_from_point_to_yellowRef, distance_to_yellowRef)
        '''
        
        # COMMENT EVERYTHING ELSE OUT IN THIS METHOD, AND UNCOMMENT THE FOLLOWING FOUR LINES
        # TO TEST THE SAME LOGIC IMPLEMENTED IN THE CONTROL PANEL SUBSYSTEM.
        # SEE ALSO __init__() METHOD
        #controlPanelSystem = subsystems.team1757Subsystems.gControlPanel
        #controlPanelSystem.updatePanelColor()
        #currentColor = controlPanelSystem.currentPanelColor
        #print(currentColor)
        #SmartDashboard.putNumber("Team1757TestColorSensorCommand.dashboard_color_sensor_detected_color", currentColor)




        print("Color: {}, IR: {}, Red: {}, Blue: {}, Green: {}, Prox: {}".format(color, ir, red, blue, green, proximity))

    def isFinished(self):
        return False

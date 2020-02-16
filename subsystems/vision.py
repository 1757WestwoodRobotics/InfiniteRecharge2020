import math
import wpilib
import time
from wpilib.command import Subsystem
from commands.vision_routine import VisionRoutine
from robotmap import max_info_list_length
from networktables import NetworkTables

class Vision(Subsystem):
    """
    Controls the vision via position PID
    """


    # name of the value in the network table?
    target_bearing = "target_bearing"
    image_count    = "image_count"

    # Add bearing and image count information to the list
    # most recent at front
    def addTargetInformationToList(self, bearing, count, listIn):
        # package the information together
        listOut = listIn
        info=(count, bearing)

        # add the information to the list
        # but don't add redundant information
        if (len(listOut)==0):
            listOut=[info]
        elif (listOut[0][0]!=count):
            listOut=[info] + listOut

        # keep the list from growing too long
        if (len(listOut)>max_info_list_length):
            listOut=listOut[0:max_info_list_length]

        return listOut

    ####################################################################################
    # check to see if the target is stable
    # duration is the number of images to check and threshold is 
    # the greatest difference between the readings that is allowed
    # while still being considered stable
    def targetStable(self, duration, threshold, listIn):
        #don't say it's stable if no info was checked
        if duration == 0 or len(listIn) == 0:
            return False, 0

        is_stable = False

        #makes sure duration to be checked isn't longer than the list's existence
        if duration > len(listIn):
            duration = len(listIn)

        #find the minimum and maximum bearings
        min_actual_bearing = 1000
        max_actual_bearing = -1000
        for i in self.target_info_list[:duration]:
            if i[1] < min_actual_bearing:
                min_actual_bearing = i[1]
            if i[1] > max_actual_bearing:
                max_actual_bearing = i[1]
        
        #find the difference between min and max bearings and use it to determine if stable
        bearing_change = max_actual_bearing - min_actual_bearing
        if bearing_change <= threshold:
            is_stable = True
        
        return is_stable, bearing_change


    def getBearingToTarget(self,listIn):
        if (len(listIn)>0):
            bearing=listIn[0][0]
            count=listIn[0][1]
        return bearing, count
    ########################################################################################
    # this reads the network table to get the most recent bearing to the target
    # the bearing is in degress. + is clockwiese, - counter clockwise
    def add_target_info_to_list(self,listIn):
        bearing = self.SmartDashboard.getNumber(Vision.target_bearing, 0)
        count = self.SmartDashboard.getNumber(Vision.image_count,0)
        listOut = self.addTargetInformationToList(bearing, count, listIn)
        return listOut

    ####################################################################################
    # locate the target and rotate the turret to it
    # returns True, if the target is within the threshold after targetting
    # threshold is in degrees
    def lock_on_target(self,threshold,listIn):

        # assume you are not on target and something is wrong
        on_target=False

        # wait for a stable image
        checks = 0
        stable=False
        while (stable==False and checks<10):
            stable, difference=self.targetStable(3,threshold,listIn)
            checks += 1
            time.sleep(0.5)

        target_bearing=self.getBearingToTarget()
        
        # if the image is stable then rotate the turret
        if (stable):
            rotate_by_angle(target_bearing)

        # after rotating, check to see if you are on target
        # wait for a stable image
        checks = 0
        stable=False
        while (stable==False and checks<10):
            stable, difference=self.targetStable(3,threshold,listIn)
            checks += 1
            time.sleep(0.5)

        target_bearing=self.getBearingToTarget()

        if (abs(target_bearing)<threshold):
            on_target=True

    
        return on_target, target_bearing

    def __init__(self):
        """Instantiates the motor object."""
        Subsystem.__init__(self, "Vision")
        NetworkTables.initialize(server = "127.0.0.1")
        self.SmartDashboard = NetworkTables.getTable("SmartDashboard")

    def initDefaultCommand(self):
        self.setDefaultCommand(VisionRoutine())

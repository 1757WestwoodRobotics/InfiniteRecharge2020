import wpilib

# Team 1757 stuff
import subsystems.team1757Subsystems
import commands.team1757TestColorSensor


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        subsystems.team1757Subsystems.init()

        self.colorSensorTester = Team1757TestColorSensor()

    # def robotPeriodic(self):
    #     # Get the sensor attributes
    #     color = self.colorSensor.getColor()
    #     ir = self.colorSensor.getIR()

    #     # Get the individual components of the color
    #     red = color.red
    #     blue = color.blue
    #     green = color.green

    #     # Get the approximate proximity of an object
    #     proximity = self.colorSensor.getProximity()

    def testInit(self):
        self.colorSensorTester.start()



if __name__ == "__main__":
    wpilib.run(Robot)

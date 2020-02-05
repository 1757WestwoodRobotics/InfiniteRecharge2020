import wpilib
from rev.color import ColorSensorV3


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    def robotPeriodic(self):
        # Get the sensor attributes
        color = self.colorSensor.getColor()
        ir = self.colorSensor.getIR()

        # Get the individual components of the color
        red = color.red
        blue = color.blue
        green = color.green

        # Get the approximate proximity of an object
        proximity = self.colorSensor.getProximity()
        
if __name__ == "__main__":
    wpilib.run(Robot)

import collections


# This is better way to set up constants, similar to an enum in Java or C++
# Tuples are immutable, so you don't have to worry about someone accidentally overwriting their values.
# They are truly constant.  Also, the syntax for using the values is cleaner than for a dictionary, e.g.
# value = Can.leftFront
# Code style point: Capitalizing the first letter also makes them stand out in your code as constants.
Can = collections.namedtuple("_", ("leftFront "
                                   "rightFront "
                                   "leftBack "
                                   "rightBack "
                                   "collector "
                                   "ballholder1 "
                                   "ballholder2 "
                                   "ballShooterLower "
                                   "ballShooterUpper "
                                   "turret "
                                   "controlPanel "
                                   "lift1 "
                                   "lift2")) (*range(13))


# Constants required by /associated with the ControlPanel subsystem and command.
# Members:
#    PanelColors: the four colors, accessed like this: ColorPanelConst.PanelColors.Red
#    Threshold: Minimum R, G, B or (R and G) value to indicate Red, Green, Blue or Yellow detected.
#               (this is pretty simplistic and can be replaced with something better later)
#    RotationSense: Should be +/-1  (easy way to switch positive and negative rotation conventions)
ColorPanelConst = (collections.namedtuple("_", ("PanelColors "
                                               "Threshold "
                                               "RotationSense"))
                                               (collections.namedtuple("_", "Red Green Blue Yellow") (*range(4)),
                                               0.5,
                                               1))

PCM1 = collections.namedtuple("_", ("Compressor" 
                                    "DiscBrakeF"
                                    "DiskBrakeB"
                                    "BallRelease1F"
                                    "BallRelease1B"
                                    "BallRelease2F"
                                    "BallRelease2B")) (*range(7))
                                    

                                               

NeutralModes = collections.namedtuple("_", "Coast Brake") (*range(2))
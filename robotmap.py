import collections

from libs1757.vector import Vector

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
                                   "PCM")) (*range(13))

xboxButtons = collections.namedtuple("_", "A B X Y LB RB Back Start LStick RStick") (1,2,3,4,5,6,7,8,9,10)

xboxAxes = collections.namedtuple("_", "LSX LSY LT RT RSX RSY") (*range(6))


# Constants required by /associated with the ControlPanel subsystem and command.
# Members:
#    PanelColors: the four colors, accessed like this: ColorPanelConst.PanelColors.Red
#    Threshold: Minimum R, G, B or (R and G) value to indicate Red, Green, Blue or Yellow detected.
#               (this is pretty simplistic and can be replaced with something better later)
#    RotationSense: Should be +/-1  (easy way to switch positive and negative rotation conventions)
ColorPanelConst = (collections.namedtuple("_", ("PanelColors "
                                                "ReferenceRed "
                                                "ReferenceGreen "
                                                "ReferenceBlue "
                                                "ReferenceYellow "
                                                "RotationSense"))
                                                (collections.namedtuple("_", "Red Green Blue Yellow Junk Reset") (*range(6)),
                                                 Vector(0.512329,0.348755,0.139038),
                                                 Vector(0.168579,0.574585,0.256958),
                                                 Vector(0.127319,0.423462,0.449097),
                                                 Vector(0.316284,0.556763,0.126831),
                                                 1))

PCM = collections.namedtuple("_", ("IndexerF "
                                    "IndexerR "
                                    "DiscBrakeF "
                                    "DiscBrakeR "
                                    "ControlPanelF "
                                    "ControlPanelR "
                                    "CollectorF "
                                    "CollectorR")) (*range(8))
                                               

NeutralModes = collections.namedtuple("_", "Coast Brake") (*range(2))
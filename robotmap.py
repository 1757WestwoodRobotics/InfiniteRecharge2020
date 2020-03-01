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
                                   "lift1 "
                                   "PCM")) (*range(12))

xboxButtons = collections.namedtuple("_", "A B X Y LB RB Back Start LStick RStick") (*range(1, 11))

xboxAxes = collections.namedtuple("_", "LSX LSY LT RT RSX RSY") (*range(6))


# Constants required by /associated with the ControlPanel subsystem and command.
# Members:
#    PanelColors: the four colors, plus two extra references, accessed like this: ColorPanelConst.PanelColors.Red
#    ReferenceRed, ReferenceGreen, ReferenceBlue, ReferenceYellow: (R,G,B) vectors which hold the expected R,G,B
#    values when the sensor is pointed at the Red, Green, Blue, Yellow octants on the control panel wheel.
#    NOTE: THESE SHOULD BE ADJUSTED IN EACH NEW LIGHTING ENVIRONMENT!
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
                                    "CollectorF "
                                    "CollectorR")) (*range(6))

ControlSystem = collections.namedtuple("_", (   "Switch1 " 
                                                "Switch2 "
                                                "Switch3 "
                                                "Switch4 "
                                                "Switch5 "
                                                "Switch6 "
                                                "Button1 "
                                                "Button2 "
                                                "Button3 "
                                                "Button4 "
                                                "Button5 "
                                                "Button6 "
                                                "Button7 "
                                                "Button8 "
                                                "Button9 ")) (*range(1, 16))
                                               

NeutralModes = collections.namedtuple("_", "Coast Brake") (*range(2))

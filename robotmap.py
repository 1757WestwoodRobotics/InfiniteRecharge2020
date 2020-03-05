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
                                   "ballholder1 "
                                   "ballholder2 "
                                   "ballShooterLower "
                                   "ballShooterUpper "
                                   "turret "
                                   "lift1 "
                                   "brake")) (*range(11))

xboxButtons = collections.namedtuple("_", "A B X Y LB RB Back Start LS RS") (*range(1, 11))

ControlSystem = collections.namedtuple("_", (   "SwitchE " 
                                                "SwitchD "
                                                "SwitchC "
                                                "SwitchB "
                                                "SwitchA "
                                                "BottomLeft "
                                                "TopLeft "
                                                "BottomRight "
                                                "TopRight "
                                                "TopMiddle "
                                                "BottomMiddle ")) (*range(1, 12))
                                               

NeutralModes = collections.namedtuple("_", "Coast Brake") (*range(2))

import collections

#can = {
#    "leftFront": 0,
#    "rightFront": 1,
#    "leftBack": 2,
#    "rightBack": 3,
#    "ballshooter1": 4,
#    "ballshooter2": 5,
#    "controlPanel": 6
#}

# This is better way to set up constants, similar to an enum in Java or C++
# Tuples are immutable, so you don't have to worry about someone accidentally overwriting their values.
# They are truly constant.  Also, the syntax for using the values is cleaner than for a dictionary, e.g.
# value = Can.LeftFront
# Code style point: Capitalizing the first letter also makes them stand out in your code as constants.
Can = collections.namedtuple("_", "leftFront rightFront leftBack rightBack collector ballholder1 ballholder2 ballShooterLower ballShooterUpper turret controlPanel lift1 lift2") (*range(13))


colors = {
    "red": 0,
    "green": 1,
    "blue": 2,
    "yellow": 3
}

#neutralModes = {
#    "coast": 1,
#    "brake": 2
#}
NeutralModes = collections.namedtuple("_", "Coast Brake") (*range(2))
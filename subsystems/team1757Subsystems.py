# Westwood FRC Team 1757
# 2020

# A central place to activate all subsystems required by the robot.
#
# OK, so what do I do?
#
# (1) 'import' your Subsystem type
# (2) declare an instance of your Subsystem type and set it to None
# (3) In the init() function:
#        - declare your instance as 'global'
#        - instantiate your instance by call its constructor
#     (The init() function is called from our robotInit() function)
#
# P.S. There's probably a better way to do this than rely on 'global' (yuck)
#      but we can always revisit this later.

import subsystems.drivetrain
import subsystems.turret
import subsystems.pneumaticsbase
import subsystems.shooter
import subsystems.lift
import subsystems.ballloader
import subsystems.ballcollector

turret = None
drivetrain = None
pneumatics = None
shooter = None
pneumaticsBase = None
lift = None
ballLoader = None
ballCollector = None

def init():
    global turret
    global drivetrain
    global pneumatics
    global shooter
    global pneumaticsBase
    global lift
    global ballLoader
    global ballCollector

    drivetrain = subsystems.drivetrain.Drivetrain()
    turret = subsystems.turret.Turret()
    pneumatics = subsystems.pneumaticsbase.PneumaticsBase()
    shooter = subsystems.shooter.Shooter()
    pneumaticsBase = subsystems.pneumaticsbase.PneumaticsBase()
    lift = subsystems.lift.Lift()
    ballLoader = subsystems.ballloader.BallLoader()
    ballCollector = subsystems.ballcollector.BallCollector()
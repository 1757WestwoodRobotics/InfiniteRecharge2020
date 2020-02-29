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

import subsystems.colorsensor
import subsystems.drivetrain
import subsystems.turret
import subsystems.pneumaticsbase
import subsystems.indexer
import subsystems.controlpanel
import subsystems.lift


gREVColorSensor = None
turret = None
drivetrain = None
controlPanel = None
pneumaticsBase = None
indexer = None
lift = None

def init():
    global gREVColorSensor
    global turret
    global drivetrain
    global controlPanel
    global pneumaticsBase
    global indexer
    global lift

    gREVColorSensor = subsystems.colorsensor.ColorSensorSubsystem()
    drivetrain = subsystems.drivetrain.Drivetrain()
    turret = subsystems.turret.Turret()
    controlPanel = subsystems.controlpanel.ControlPanel()
    pneumaticsBase = subsystems.pneumaticsbase.PneumaticsBase()
    indexer = subsystems.indexer.Indexer()
    lift = subsystems.lift.Lift()
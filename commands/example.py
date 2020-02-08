from wpilib.command import InstantCommand


class Example(InstantCommand):
    """
    Causes an exception when activated. Not likely to be useful, but it's a
    simple way to test if exception recovery is working.
    """

    def __init__(self):
        InstantCommand.__init__(self, "Example Command")

    def initialize(self):
        print("Example Command Executed")

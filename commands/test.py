import wpilib
from wpilib.command import Command

class Test(Command):
    '''
    Command to test oi inputs, which prints messages within each section of the command
    '''

    def __init__(self):
        Command.__init__(self, "Test")

        print("Init")

    def initialize(self):
        print("Initialize")

    def execute(self):
        print("Execute")

    def end(self):
        print("End")

    def isFinished(self):
        return False
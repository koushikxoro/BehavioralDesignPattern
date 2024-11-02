from command import Command
from light import Light
class OnCommand(Command):
    def __init__(self, light:Light):
        self.light=light
    def execute(self):
        self.light.turn_on()
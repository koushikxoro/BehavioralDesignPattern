from oncommand import OnCommand
from offcommand import OffCommand
from invoker import RemoteControl
from light import Light
if __name__=="__main__":
    #create a receiver
    light=Light()

    #create command objects
    light_on=OnCommand(light)
    light_off=OffCommand(light)

    #create an invoker
    remote=RemoteControl()

    #Turn the light on
    remote.set_command(light_on)
    remote.press_button()

    #Turn the light off
    remote.set_command(light_off)
    remote.press_button()

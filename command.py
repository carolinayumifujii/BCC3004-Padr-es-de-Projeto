# Command Interface
class Command:
    def execute(self):
        pass

# Receiver
class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")

# Concrete Command for turning on the light
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

# Concrete Command for turning off the light
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    # Turn the light on
    remote.set_command(light_on)
    remote.press_button()

    # Turn the light off
    remote.set_command(light_off)
    remote.press_button()

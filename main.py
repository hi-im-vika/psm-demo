import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        self.term = Terminal()
        self.spacemouse = pyspacemouse.open()

    def run(self):
        print("Hello from psm-demo!")


if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
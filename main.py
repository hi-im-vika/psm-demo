import time
import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        self.term = Terminal()
        self.spacemouse = pyspacemouse.open()

    def run(self):
        print("Hello from psm-demo!")
        with pyspacemouse.open() as spacemouse:
            while True:
                print("pyspacemouse")
                time.sleep(1)
        self.cleanup()

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
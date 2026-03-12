import time
import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        self.term = Terminal()
        self.spacemouse = pyspacemouse.open()

    def run(self):
        print("Hello from psm-demo!")
        with (self.term.fullscreen(), 
              self.term.hidden_cursor(), 
              pyspacemouse.open() as self.spacemouse):
            while True:
                print("pyspacemouse")
                time.sleep(1)
        self.cleanup()

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        self.term = Terminal()
        self.spacemouse = pyspacemouse.open()

    def run(self):
        print("Hello from psm-demo!")
        self.cleanup()

    def cleanup(self):
        print("Cleaning up...")
        try:
            self.spacemouse.close()
        except:
            print("Error closing spacemouse. Is it connected?")

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
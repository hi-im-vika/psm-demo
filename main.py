import time
import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        self.term = Terminal()

    def _draw(self):
        x = self.term.width // 2
        y = self.term.height // 2

        state = self.spacemouse.read()
        xyz = [state.x, state.y, state.z]

        label = "pyspacemouse state"
        with self.term.location(x - len(label) // 2, y - 1):
            print(self.term.bold_cyan(label))

        for i, axis in enumerate("XYZ"):
            with self.term.location(x - 4, y + 1 + i):
                print(self.term.bold_white("{}: {:.2f}".format(axis, xyz[i])))

        with self.term.location(x - 9, y + 5):
            print("Press Ctrl+C to exit")

    def run(self):
        print("Hello from psm-demo!")
        with (pyspacemouse.open() as self.spacemouse,
              self.term.fullscreen(), 
              self.term.hidden_cursor(), ):
            while True:
                self._draw()
        self.cleanup()

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
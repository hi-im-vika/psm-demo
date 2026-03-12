import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        self.term = Terminal()
        self.spacemouse = None

    def _draw(self):
        x = self.term.width // 2
        y = self.term.height // 2

        state = self.spacemouse.read()
        xyz = [state.x, state.y, state.z]
        rpy = [state.roll, state.pitch, state.yaw]
        rpy_labels = ["R", "P", "Y"]

        label = "pyspacemouse state"
        with self.term.location(x - len(label) // 2, y - 1):
            print(self.term.bold_cyan(label))

        for i, axis in enumerate("XYZ"):
            line = "{}: {: .2f}    {}: {: .2f}".format(
                axis, xyz[i], rpy_labels[i], rpy[i]
            )
            with self.term.location(x - len(line) // 2, y + 1 + i):
                print(self.term.bold_white(line))

        with self.term.location(x - 9, y + 5):
            print("Press Ctrl+C to exit")

    def run(self):
        print("Hello from psm-demo!")
        with (pyspacemouse.open() as self.spacemouse,
              self.term.fullscreen(), 
              self.term.hidden_cursor()):
            while True:
                self._draw()

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
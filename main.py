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

        lines = []
        for i, axis in enumerate("XYZ"):
            lines.append("{}: {: .2f}    {}: {: .2f}".format(
                axis, xyz[i], rpy_labels[i], rpy[i]
            ))

        inner_width = max(len(label), max(len(l) for l in lines))
        box_x = x - (inner_width + 2) // 2

        with self.term.location(box_x, y - 1):
            print("┌" + "─" * (inner_width + 2) + "┐")

        with self.term.location(box_x, y):
            print("│ " + self.term.bold_cyan(label.center(inner_width)) + " │")

        with self.term.location(box_x, y + 1):
            print("├" + "─" * (inner_width + 2) + "┤")

        for i, line in enumerate(lines):
            with self.term.location(box_x, y + 2 + i):
                print("│ " + self.term.bold_white(line.center(inner_width)) + " │")

        with self.term.location(box_x, y + 2 + len(lines)):
            print("└" + "─" * (inner_width + 2) + "┘")

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
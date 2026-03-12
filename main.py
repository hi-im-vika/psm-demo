import pyspacemouse
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual import work

class PSMDisplay(Static):
    pass

class PSMDemoApp(App):
    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
        ("ctrl+q", "noop", ""),
    ]

    def compose(self) -> ComposeResult:
        yield PSMDisplay()

    def action_noop(self) -> None:
        pass

    def on_mount(self) -> None:
        self.spacemouse = pyspacemouse.open()
        self.poll()

    @work(thread=True)
    def poll(self) -> None:
        display = self.query_one(PSMDisplay)
        while True:
            state = self.spacemouse.read()
            display.xyz = [state.x, state.y, state.z]
            display.rpy = [state.roll, state.pitch, state.yaw]

    def on_unmount(self) -> None:
        pass

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
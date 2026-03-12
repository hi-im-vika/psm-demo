import pyspacemouse
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.reactive import reactive
from textual import work

class PSMDisplay(Static):
    xyz = reactive([0.0, 0.0, 0.0])
    rpy = reactive([0.0, 0.0, 0.0])

    def render(self):
        rpy_labels = ["R", "P", "Y"]
        lines = []
        for i, axis in enumerate("XYZ"):
            lines.append(
                f"[bold]{axis}[/bold]: {self.xyz[i]: .2f}    "
                f"[bold]{rpy_labels[i]}[/bold]: {self.rpy[i]: .2f}"
            )
        return (
            "[bold cyan]pyspacemouse state[/bold cyan]\n\n"
            + "\n".join(lines)
            + "\n\n[dim]Press Ctrl+C to exit[/dim]"
        )

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
        self.spacemouse.close()

if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
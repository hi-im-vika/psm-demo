import pyspacemouse
from blessed import Terminal

class PSMDemoApp:
    def __init__(self):
        pass

    def run(self):
        print("Hello from psm-demo!")


if __name__ == "__main__":
    try:
        PSMDemoApp().run()
    except KeyboardInterrupt:
        pass
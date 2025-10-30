import logging
logging.basicConfig(level=logging.INFO)

from frangipani.launcher import Launcher


if __name__ == "__main__":
    launcher = Launcher()
    launcher.launch()

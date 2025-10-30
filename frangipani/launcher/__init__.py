from PySide6.QtWidgets import QApplication

from pyside6helpers import css
from pyside6helpers.main_window import MainWindow

from frangipani.central_widget import CentralWidget
from frangipani.components import api as components_api


class Launcher:

    def launch(self):
        app = QApplication()
        app.setApplicationName("Frangipani")
        app.setOrganizationName("Frangitron")
        css.load_onto(app)

        main_window = MainWindow()
        main_window.firstTimeShown.connect(components_api.init_components)
        main_window.setCentralWidget(CentralWidget())
        main_window.show()

        app.exec()

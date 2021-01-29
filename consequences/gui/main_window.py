import pathlib
import sys
from PySide6 import QtWidgets

from consequences.gui.dir_load_widget import loadWindow
from consequences.gui.gameplay_widget import gameplayWidget


def open_window():
    qt_app = QtWidgets.QApplication([])

    # main_window = loadWindow()

    # For testing
    contentpath = pathlib.Path() / 'consequences' / 'content' / 'template.json'

    main_window = gameplayWidget(contentpath)

    main_window.setWindowTitle("Consequences")
    main_window.show()

    sys.exit(qt_app.exec_())

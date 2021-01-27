import sys
from PySide6 import QtWidgets  # QtCore,

from consequences.gui.dir_load_widget import loadWindow


def open_window():
    qt_app = QtWidgets.QApplication([])

    main_window = loadWindow()

    main_window.setWindowTitle("Consequences")
    main_window.show()

    sys.exit(qt_app.exec_())

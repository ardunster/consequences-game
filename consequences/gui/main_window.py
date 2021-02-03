import pathlib
import sys
from PySide6 import QtWidgets, QtCore

from consequences.gui.dir_load_widget import loadWindow
from consequences.gui.gameplay_widget import gameplayWidget


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.load = loadWindow()

        self.stacked = QtWidgets.QStackedWidget()
        self.stacked.addWidget(self.load)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.stacked)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.load.content.story_select_button.clicked.connect(self.select_content)
        self.load.output.story_select_button.clicked.connect(self.select_output)

    @QtCore.Slot()
    def select_content(self):
        self.content_func(self.load.content.content_list.target)

    @QtCore.Slot()
    def select_output(self):
        self.content_func(self.load.output.content_list.target)

    def content_func(self, input_path):
        if input_path == "" or input == "Error":
            print("Please select a list item.")
        else:
            self.game = gameplayWidget(input_path)
            self.stacked.addWidget(self.game)
            self.stacked.setCurrentWidget(self.game)
            print(f"Story Select: {input_path}")


def open_window():
    qt_app = QtWidgets.QApplication([])

    main_window = mainWindow()

    main_window.setWindowTitle("Consequences")
    main_window.show()

    sys.exit(qt_app.exec_())

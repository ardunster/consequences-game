import sys
from PySide6 import QtWidgets, QtCore

from consequences.common.generate import generate
from consequences.common.files import output_save, output_load, directory_load
from consequences.gui.dir_load_widget import loadWindow
from consequences.gui.gameplay_widget import gameplayWidget
from consequences.gui.output_display_widget import outputDisplay

# TODO: Implement a popup box for the "please select a list item" spots


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.load = loadWindow()
        self.preload()

        self.stacked = QtWidgets.QStackedWidget()
        self.stacked.addWidget(self.load)
        self.stacked.addWidget(self.game)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.stacked)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.load.content.story_select_button.clicked.connect(self.select_content)
        self.load.output.story_select_button.clicked.connect(self.select_output)

    def preload(self):
        """
        Pre loads the gameplay window with whatever the first item in the load
        window will be. Workaround for a graphics inconsistency if game window
        is not preloaded.
        """
        contentpath = list(self.load.content.content_list.contents.items())[0][1]
        self.game = gameplayWidget(contentpath)

    def setup_gameplay(self, input_path):
        self.game = gameplayWidget(input_path)
        self.stacked.addWidget(self.game)
        self.stacked.setCurrentWidget(self.game)

        self.game.cancel_button.clicked.connect(self.cancel)
        self.game.generate_button.clicked.connect(self.generate_output)

    @QtCore.Slot()
    def select_content(self):
        input_path = self.load.content.content_list.target
        if input_path == "" or input_path == "Error":
            print("Please select a list item.")
        else:
            self.setup_gameplay(input_path)
            print(f"Story Select: {input_path}")

    @QtCore.Slot()
    def select_output(self):
        input_path = self.load.output.content_list.target
        if input_path == "" or input_path == "Error":
            print("Please select a list item.")
            return
        else:
            loaded = output_load(input_path)
            output_display = outputDisplay(loaded, True)
            print(f"Story Select: {input_path}")
        ret = output_display.exec_()
        if ret == QtWidgets.QMessageBox.Save:
            pass
        elif ret == QtWidgets.QMessageBox.AcceptRole:
            self.cancel()
        else:
            pass

    @QtCore.Slot()
    def cancel(self):
        self.stacked.setCurrentWidget(self.load)

    @QtCore.Slot()
    def generate_output(self):
        # Retrieve content from form and update dictionary, generate and display
        # the output, give option to save.
        for i in range(self.game.form_layout.rowCount()):
            self.game.content["values"][
                self.game.edit_list[i][0].text()
            ] = self.game.edit_list[i][1].text()
        generated = generate(self.game.content)
        output_display = outputDisplay(generated)
        ret = output_display.exec_()
        if ret == QtWidgets.QMessageBox.Save:
            print("Saving...")
            output_save(generated)
            self.load.output.content_list.contents = directory_load(
                self.load.output.directory
            )
            # TODO: Figure out what's missing to make this actually reload the
            # content list after safing a new file.
            # TODO: make this not automatically close the message box?
        elif ret == QtWidgets.QMessageBox.AcceptRole:
            self.cancel()
        else:
            pass


def open_window():
    qt_app = QtWidgets.QApplication([])

    main_window = mainWindow()

    main_window.setWindowTitle("Consequences")
    main_window.show()

    sys.exit(qt_app.exec_())

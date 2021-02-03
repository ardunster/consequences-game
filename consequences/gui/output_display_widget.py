from PySide6 import QtWidgets

import consequences.common.generate
import consequences.common.files_load


class outputDisplay(QtWidgets.QMessageBox):
    def __init__(self, display_dictionary, from_load=False):
        super().__init__()
        self.display_dictionary = display_dictionary
        self.from_load = from_load

        self.setWindowTitle("Results!")
        self.setText(self.display_dictionary['title'])
        self.setInformativeText(self.display_dictionary['text'])

        self.addButton("Return to main screen", QtWidgets.QMessageBox.AcceptRole)

        # Only allow Save if new content generated, to avoid duplicate output
        if self.from_load == False:
            self.addButton(QtWidgets.QMessageBox.Save)
            self.setDefaultButton(QtWidgets.QMessageBox.Save)
            self.addButton(QtWidgets.QMessageBox.Cancel)

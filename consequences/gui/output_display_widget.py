from PySide6 import QtWidgets


class outputDisplay(QtWidgets.QMessageBox):
    def __init__(self, display_dictionary, from_load=False):
        super().__init__()
        self.display_dictionary = display_dictionary
        self.from_load = from_load

        self.setWindowTitle("Results!")
        self.setText(self.display_dictionary["title"])

        # Construct and display output string
        display_text = self.display_dictionary["text"]
        if "Made by:" in self.display_dictionary:
            display_text += "\nMade by: " + self.display_dictionary["Made by:"]
        display_text += (
            "\nMade on: "
            + display_dictionary["time"].strftime("%D")
            + " at "
            + display_dictionary["time"].strftime("%H:%M")
        )

        self.setInformativeText(display_text)

        # Only allow Save if new content generated, to avoid duplicate output
        if not self.from_load:
            self.addButton(QtWidgets.QMessageBox.Save)
            self.setDefaultButton(QtWidgets.QMessageBox.Save)
            self.addButton(QtWidgets.QMessageBox.Cancel)

        self.addButton("Return to main screen", QtWidgets.QMessageBox.AcceptRole)

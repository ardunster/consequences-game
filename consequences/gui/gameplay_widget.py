from PySide6 import QtCore, QtWidgets

from consequences.common.files_load import content_load
from consequences.common.generate import generate
from consequences.gui.output_display_widget import outputDisplay


class gameplayWidget(QtWidgets.QWidget):
    def __init__(self, content_filepath):
        super().__init__()

        # Fetch content from selected file
        self.content = content_load(content_filepath)
        self.title = QtWidgets.QLabel(self.content['title'])

        # Lay out the form
        self.edit_list = []
        self.form_layout = QtWidgets.QFormLayout()
        for k, v in self.content['values'].items():
            label_widget = QtWidgets.QLabel(k)
            line_edit_widget = QtWidgets.QLineEdit(v)
            self.form_layout.addRow(label_widget, line_edit_widget)
            self.edit_list.append((label_widget, line_edit_widget))

        # Lay out the buttons
        self.cancel_button = QtWidgets.QPushButton("&Cancel")
        self.generate_button = QtWidgets.QPushButton("&Generate!")
        self.generate_button.setDefault(True)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.generate_button)

        # Outer layout with buttons
        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(self.title, alignment=QtCore.Qt.AlignCenter)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

        # Button connects
        self.cancel_button.clicked.connect(self.cancel)
        self.generate_button.clicked.connect(self.generate)

    @QtCore.Slot()
    def cancel(self):
        print("Cancel pressed")
        # How do I go back to the previous screen from here?

    @QtCore.Slot()
    def generate(self):
        # Retrieve content from form and update dictionary, generate and display
        # the output, give option to save.
        for i in range(self.form_layout.rowCount()):
            self.content['values'][self.edit_list[i][0].text()] = self.edit_list[i][1].text()
        generated = generate(self.content)
        output_display = outputDisplay(generated)
        ret = output_display.exec_()
        if ret == QtWidgets.QMessageBox.Save:
            # TODO: call save function with generated dict
            print("Save clicked")
        elif ret == QtWidgets.QMessageBox.AcceptRole:
            # TODO: Figure out how to make this go back to the main screen
            print("Return clicked")
        else:
            # Error throw?
            print("Something else clicked (?????)")

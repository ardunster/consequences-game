from PySide6 import QtCore, QtWidgets

from consequences.common.files import content_load


class gameplayWidget(QtWidgets.QWidget):
    def __init__(self, content_filepath):
        super().__init__()

        # Fetch content from selected file
        self.content = content_load(content_filepath)
        self.title = QtWidgets.QLabel(self.content['title'])

        # Add line for Made By:
        self.content['values']["Made by:"] = "Enter name(s)"

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


import random

from PySide6 import QtCore, QtWidgets, QtGui

from consequences.common.files_load import directory_load

class dirLoadWidget(QtWidgets.QWidget):
    def __init__(self, which_dir):
        super().__init__()

        # Load contents of the selected directory
        self.contents = directory_load(which_dir)

        # self.button = QtWidgets.QPushButton("push it")
        # self.text = QtWidgets.QLabel("the label",
        #                              alignment=QtCore.Qt.AlignCenter)

        # Create list widget and populate it with the directory information
        self.list = QtWidgets.QListWidget(self)
        self.list.addItems(self.contents)

        # self.layout = QtWidgets.QVBoxLayout()

        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        # self.setLayout(self.layout)

    # @QtCore.Slot()
    # def magic(self):
    #     self.text.setText(random.choice(self.contents))
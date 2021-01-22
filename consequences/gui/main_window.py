import sys
from PySide6 import QtCore, QtWidgets, QtGui

from consequences.gui.dir_load_widget import dirLoadWidget

# make list + button classes here

class ContentList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel("Available Stories",
                                     alignment=QtCore.Qt.AlignCenter)
        label.setMaximumHeight(15)

        # Get content directory contents
        content_list = dirLoadWidget("fred")
        content_list.setMinimumHeight(100)

        # Create "Select Story" button
        story_select_button = QtWidgets.QPushButton("Start Selected Story")
        story_select_button.setMaximumHeight(50)

        # add to layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5,5,5,5)
        layout.setSpacing(5)
        layout.addWidget(label)
        layout.addWidget(content_list)
        layout.addWidget(story_select_button)
        self.setLayout(layout)

        story_select_button.clicked.connect(self.select)

    @QtCore.Slot()
    def select(self):
        print("Story Selected")

class OutPutList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel("Saved Stories",
                                     alignment=QtCore.Qt.AlignCenter)
        label.setMaximumHeight(15)

        # Get content directory contents
        content_list = dirLoadWidget("steve")
        content_list.setMinimumHeight(100)

        # Create "Read Story" button
        story_select_button = QtWidgets.QPushButton("Read Saved Story")
        story_select_button.setMaximumHeight(50)

        # add to layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5,5,5,5)
        layout.setSpacing(5)
        layout.addWidget(label)
        layout.addWidget(content_list)
        layout.addWidget(story_select_button)
        self.setLayout(layout)

        story_select_button.clicked.connect(self.read)

    @QtCore.Slot()
    def read(self):
        print("Read Story Selected")

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Get directory contents - these will probably be further subdivided by
        # more widgets containing relevant buttons in vertical box layouts
        content = ContentList()
        output = OutPutList()

        # Add to sub layout
        sub_layout = QtWidgets.QHBoxLayout()
        sub_layout.setContentsMargins(5,5,5,5)
        sub_layout.setSpacing(5)
        sub_layout.addWidget(content)
        sub_layout.addWidget(output)

        # Create top banner and outer layout and configure.
        banner = QtWidgets.QLabel("Welcome to the Consequences Game!")
        banner.setMaximumHeight(10)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5,5,5,5)
        layout.setSpacing(5)
        layout.addWidget(banner)
        layout.addLayout(sub_layout)
        self.setLayout(layout)

def open_window():
    qt_app = QtWidgets.QApplication([])

    main_window = MainWindow()

    main_window.setWindowTitle("Consequences")
    # main_window.resize(500, 500)
    main_window.show()

    sys.exit(qt_app.exec_())

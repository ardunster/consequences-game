from PySide6 import QtCore, QtWidgets  # , QtGui

from consequences.common.files_load import directory_load


class dirLoadWidget(QtWidgets.QWidget):
    def __init__(self, which_dir):
        super().__init__()

        # Load contents of the selected directory
        self.contents = directory_load(which_dir)

        # Create list widget and populate it with the directory information
        self.list = QtWidgets.QListWidget(self)
        for k, v in self.contents.items():
            item = QtWidgets.QListWidgetItem(k)
            item.setData(1, v)
            self.list.addItem(item)

        self.target = ""

        self.list.clicked.connect(self.clicked_list_item)

    @QtCore.Slot()
    def clicked_list_item(self):
        self.target = self.list.currentItem().data(1)
        print(f"clicked a list item {self.target}")


class ListBox(QtWidgets.QWidget):
    def __init__(self, title, directory, button_text, select_func):
        super().__init__()

        # Initialize variables
        self.title = title
        self.directory = directory
        self.button_text = button_text
        self.select_func = select_func

        # Build list label
        self.label = QtWidgets.QLabel(self.title,
                                      alignment=QtCore.Qt.AlignCenter)
        self.label.setMaximumHeight(15)

        # Get specified directory contents
        self.content_list = dirLoadWidget(self.directory)
        self.content_list.setMinimumHeight(100)

        # Create button
        self.story_select_button = QtWidgets.QPushButton(self.button_text)
        self.story_select_button.setMaximumHeight(50)

        # add to layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.content_list)
        self.layout.addWidget(self.story_select_button)
        self.setLayout(self.layout)

        self.story_select_button.clicked.connect(self.select)

    @QtCore.Slot()
    def select(self):
        self.select_func(self.content_list.target)


def content_func(input):
    # temp text func for select button
    if input == "":
        print("Please select a list item.")
    else:
        print(f"Story Select: {input}")


class loadWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Get directory contents
        self.content = ListBox("Available Stories",
                               "content", "Start Selected Story",
                               content_func)
        # content = ContentList()
        self.output = ListBox("Saved Stories",
                              "output", "Read Saved Story",
                              content_func)

        # Add to sub layout
        self.sub_layout = QtWidgets.QHBoxLayout()
        self.sub_layout.setContentsMargins(5, 5, 5, 5)
        self.sub_layout.setSpacing(5)
        self.sub_layout.addWidget(self.content)
        self.sub_layout.addWidget(self.output)

        # Create top banner and outer layout and configure.
        self.banner = QtWidgets.QLabel("Welcome to the Consequences Game!",
                                       alignment=QtCore.Qt.AlignCenter)
        self.banner.setMaximumHeight(10)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)
        self.layout.addWidget(self.banner)
        self.layout.addLayout(self.sub_layout)
        self.setLayout(self.layout)

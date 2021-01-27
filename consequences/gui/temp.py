

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        load_window = loadWindow
        self.setLayout(load_window)
        does this need renamed as it's only the initial window not always the
        main window?

        # Get directory contents
        content = ListBox("Available Stories",
                          "fred", "Start Selected Story",
                          content_func)
        # content = ContentList()
        output = ListBox("Saved Stories",
                         "steve", "Read Saved Story",
                         content_func)

        # Add to sub layout
        sub_layout = QtWidgets.QHBoxLayout()
        sub_layout.setContentsMargins(5, 5, 5, 5)
        sub_layout.setSpacing(5)
        sub_layout.addWidget(content)
        sub_layout.addWidget(output)

        # Create top banner and outer layout and configure.
        banner = QtWidgets.QLabel("Welcome to the Consequences Game!",
                                  alignment=QtCore.Qt.AlignCenter)
        banner.setMaximumHeight(10)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        layout.addWidget(banner)
        layout.addLayout(sub_layout)
        self.setLayout(layout)
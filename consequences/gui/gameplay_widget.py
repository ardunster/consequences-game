from PySide6 import QtCore, QtWidgets  # , QtGui

from consequences.common.files_load import content_load
from consequences.gui.output_display_widget import outputDisplay

# Use Q Form Layout

class gameplayWidget(QtWidgets.QWidget):
    def __init__(self, content_filepath):
        super().__init__()

        # Fetch content from selected file
        self.content = content_load(content_filepath)

        self.title = QtWidgets.QLabel(content['title'])

        # Lay out the form
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.addRow("thing", "stuff")
        # add each k:v in content['values'] to form
        # when text is changed in value, and typing stop, or click out of box,
        # update value in content['values']

        # Outer layout with buttons
        self.layout = QtWidgets.QVBoxLayout()
        # add the form
        # add buttons for "cancel" and "generate", cancel goes back to load
        # window, generate calls the generate functon and creates the output box
        # with its output


# on "generate" clicked, summon the output display
        test = { "title": "Template", "text": "test with a bunch longer piece of text because who knows what will end up in here? it should handle longer text okay or else it's not very useful. Longer and longer let's make this text last foreeeeevvvveerrrrr  ......okay maybe not." }
        output_display = outputDisplay(test) #, from_load=True)
        ret = output_display.exec_()
        if ret == QtWidgets.QMessageBox.Save:
            print("save clicked")
        elif ret == QtWidgets.QMessageBox.AcceptRole:
            print("Accept clicked")
        else:
            print("Something else clicked (?????)")
from PySide6 import QtCore, QtWidgets  # , QtGui

from consequences.gui.output_display_widget import outputDisplay

# Use Q Form Layout

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
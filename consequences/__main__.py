#!./venv/bin/env python3

from consequences.common.files_load import content_load, output_load, output_save
from consequences.gui.main_window import open_window

if __name__ == '__main__':
    open_window()
    # Load welcome window
    # load files: left side content, right side output
    # populate buttons: left side new, right side load saved
    # generate
    print("welcome to game")
    pass

from time import sleep
from PyQt5.QtCore import QCoreApplication

import os
build = os.path.dirname(__file__)
from sys import path
path.insert(0, build)

from Build.Windows import MainWindow


class HelperGUI(MainWindow):
    '''
    Initialize a MainWindow and listen for changes at 200 Hertz.
    Wait till wait_for_enter is internally set to False, in which
    case return the command to cli.
    '''
    def __init__(self):
        MainWindow.__init__(self)

        self.wait_for_enter = True

    def gui_result(self, prompt):
        
        print(prompt) # >>>
        
        self.show() # >>>
        self.raise_() # >>>

        while self.wait_for_enter:
            QCoreApplication.processEvents()
            sleep(1/200)

        self.wait_for_enter = True

        return self.command_line.text()

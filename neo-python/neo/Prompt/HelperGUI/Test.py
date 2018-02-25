import sys

from prompt_toolkit.shortcuts import * # >>> needed for prompt("neo> ")
from PyQt5.QtWidgets import QApplication
from GUI import HelperGUI


class PromptInterfaceTester(HelperGUI):
    """
    If you don't want to run the GUI with the whole neo-python cli in the 
    beckground, use this class which emulates the cli-loop.
    """
    def __init__(self):
        super(PromptInterfaceTester, self).__init__()

        self.gui_on = True # >>> go on the GUI branch right from the start

    def run(self):
        print('\n')

        while True:
            if self.gui_on:
                print('gui> ')
                self.show()
                command = self.gui_result()
            else:
                command = prompt("neo> ")

            if command:
                print(command)
            if command == 'quit' or command == 'exit':
                sys.exit()
            if command == 'gui':
                self.gui_on = True


def main():

    app = QApplication(sys.argv) # >>> start gui app

    cli = PromptInterfaceTester()
    cli.run()

    app.exec_() # >>> catch gui app


if __name__ == '__main__':
    main()

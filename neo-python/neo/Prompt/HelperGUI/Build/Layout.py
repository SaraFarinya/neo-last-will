from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout

from Config import Rows


def layoutMainWindow(self):
    """
    Take all widgets defined in the main widgets function and put them in some order in the gui.
    """
    gridShortcut = QGridLayout()
    for i in Rows:
        gridShortcut.addWidget(self.line_buttons[i][0], i, 0)
        gridShortcut.addWidget(self.lines[i][0], i, 1)
        gridShortcut.addWidget(self.lines[i][1], i, 2)
        grid.addWidget(self.line_buttons[i][1], i, 3)
    gridShortcut.setSpacing(10)

    hboxCommand = QHBoxLayout()
    hboxCommand.addWidget(self.saveButton)
    hboxCommand.addWidget(self.command_line)
    hboxCommand.addWidget(self.hashButton)

    vboxAll = QVBoxLayout()
    vboxAll.addLayout(gridShortcut)
    vboxAll.addLayout(hboxCommand)

    self.setLayout(vboxAll)


def layoutDocumentWindow(self):
    """
    Take all widgets defined in the document widgets function and put them in some order in the gui.
    """
    hboxComputeHash = QHBoxLayout()
    hboxComputeHash.addStretch(1)
    hboxComputeHash.addWidget(self.hashAlgorithmBox)
    hboxComputeHash.addWidget(self.computeButton)

    vboxAll = QVBoxLayout()
    vboxAll.addWidget(self.headerLabel)
    vboxAll.addWidget(self.document_line)
    vboxAll.addWidget(self.hash_line)
    vboxAll.addLayout(hboxComputeHash)

    self.setLayout(vboxAll)

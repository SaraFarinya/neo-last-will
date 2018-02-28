from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout

from Config import Rows


def layoutMainWindow(self):
    grid = QGridLayout()
    for i in Rows:
        grid.addWidget(self.line_buttons[i][0], i, 0)
        grid.addWidget(self.lines[i][0], i, 1)
        grid.addWidget(self.lines[i][1], i, 2)
        grid.addWidget(self.line_buttons[i][1], i, 3)
    grid.setSpacing(10)

    commandHBox = QHBoxLayout()
    commandHBox.addWidget(self.saveButton)
    commandHBox.addWidget(self.command_line)
    commandHBox.addWidget(self.hashButton)

    vboxAll = QVBoxLayout()
    vboxAll.addLayout(grid)
    vboxAll.addLayout(commandHBox)

    self.setLayout(vboxAll)


def layoutDocumentWindow(self):
    computeHBox = QHBoxLayout()
    computeHBox.addStretch(1)
    computeHBox.addWidget(self.hashAlgorithmBox)
    computeHBox.addWidget(self.computeButton)

    vboxAll = QVBoxLayout()
    vboxAll.addWidget(self.headerLabel)
    vboxAll.addWidget(self.document_line)
    vboxAll.addWidget(self.hash_line)
    vboxAll.addLayout(computeHBox)

    self.setLayout(vboxAll)

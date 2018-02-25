from PyQt5.QtWidgets import QPlainTextEdit, QComboBox, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import json

from Config import Colors, Memory, Cols, Rows
import Build.Events as Events

def buildMainWindow(self):
    self.line_buffers = [['' for _ in Cols] for _ in Rows]

    self.command_line = QLineEdit(self)
    self.command_line.setStyleSheet(Colors.LineLight)

    self.saveButton = QPushButton(' Save ', self)
    self.saveButton.clicked.connect(lambda: Events.save_to_memory(self))
    self.saveButton.setStyleSheet(Colors.ButtonLight)
    self.saveButton.setFont(QFont('Helvetica', 16))

    self.hashButton = QPushButton(' Workbench ', self)
    self.hashButton.clicked.connect(lambda: Events.open_cryptography_workbench(self))
    self.hashButton.setStyleSheet(Colors.ButtonLight)
    self.hashButton.setFont(QFont('Helvetica', 16))

    self.lines = [[QLineEdit(self) for i in Cols] for j in Rows]
    def f(self, i, j, text):
        self.line_buffers[i][j] = text
    self.lines[0][0].textChanged[str].connect(lambda text: f(self, 0, 0, text))
    self.lines[1][0].textChanged[str].connect(lambda text: f(self, 1, 0, text))
    self.lines[2][0].textChanged[str].connect(lambda text: f(self, 2, 0, text))
    self.lines[3][0].textChanged[str].connect(lambda text: f(self, 3, 0, text))
    self.lines[0][1].textChanged[str].connect(lambda text: f(self, 0, 1, text))
    self.lines[1][1].textChanged[str].connect(lambda text: f(self, 1, 1, text))
    self.lines[2][1].textChanged[str].connect(lambda text: f(self, 2, 1, text))
    self.lines[3][1].textChanged[str].connect(lambda text: f(self, 3, 1, text))

    self.line_buttons = [[QPushButton('', self) for i in Cols] for j in Rows]
    def g(self, i, j):
        self.command_line.setText(self.line_buffers[i][j])
    self.line_buttons[0][0].clicked.connect(lambda: g(self, 0, 0))
    self.line_buttons[1][0].clicked.connect(lambda: g(self, 1, 0))
    self.line_buttons[2][0].clicked.connect(lambda: g(self, 2, 0))
    self.line_buttons[3][0].clicked.connect(lambda: g(self, 3, 0))
    self.line_buttons[0][1].clicked.connect(lambda: g(self, 0, 1))
    self.line_buttons[1][1].clicked.connect(lambda: g(self, 1, 1))
    self.line_buttons[2][1].clicked.connect(lambda: g(self, 2, 1))
    self.line_buttons[3][1].clicked.connect(lambda: g(self, 3, 1))

    with open(Memory, 'r') as json_file:
        memory_line = json.load(json_file)['lines']
        for i in Rows:
            for j in Cols:
                self.lines[i][j].setStyleSheet(Colors.LineDark)
                self.lines[i][j].setText(memory_line[i][j])
                self.line_buttons[i][j].setStyleSheet(Colors.ButtonDark)
    self.command_line.setText('')

def buildDocumentWindow(self):
    header = 'Author your document and compute the hash of your choice.'
    self.headerLabel = QLabel(header)
    self.headerLabel.setFont(QFont('Helvetica', 18))

    self.document_line = QPlainTextEdit(self)
    with open(Memory, 'r') as json_file:
        memory_document = json.load(json_file)['document']
    self.document_line.setPlainText(memory_document)
    self.document_line.setFixedHeight(300)
    self.document_line.setStyleSheet(Colors.LineLight)

    self.hash_line = QLineEdit(self)
    self.hash_line.setStyleSheet(Colors.LineDark)

    self.computeButton = QPushButton(' Compute ', self)
    self.computeButton.clicked.connect(lambda: Events.hash_document(self))
    self.computeButton.setStyleSheet(Colors.ButtonLight)
    self.computeButton.setFont(QFont('Helvetica', 16))

    self.hashAlgorithmBox = QComboBox(self)
    for sha in [' sha256 ', ' sha512 ']:
        self.hashAlgorithmBox.addItem(sha)
    self.hashAlgorithmBox.setStyleSheet(Colors.LineLight)

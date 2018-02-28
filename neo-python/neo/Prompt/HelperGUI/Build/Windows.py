from PyQt5.QtWidgets import QWidget

from Build.Widgets import buildMainWindow, buildDocumentWindow
from Build.Layout import layoutMainWindow, layoutDocumentWindow
from Build.Events import save_to_memory
from Config import Geometry, Colors, ConfigOS


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.gui_on = False

        self.document_window = DocumentWindow(self)

        buildMainWindow(self)
        layoutMainWindow(self)

        self.setWindowTitle('neo-python')
        self.setGeometry(*Geometry.Main)
        self.setPalette(Colors.Palette)

    def back_to_cli(self):
        save_to_memory(self)
        if self.gui_on:
            self.gui_on = False
            self.wait_for_enter = False

    def keyPressEvent(self, event):
        if self.gui_on:
            if event.key() == ConfigOS.EscapeKey:
                self.back_to_cli()
            if event.key() == ConfigOS.EnterKey:
                self.wait_for_enter = False

    def closeEvent(self, event):
        if self.gui_on:
            self.document_window.close()
            self.back_to_cli()


class DocumentWindow(QWidget):
    def __init__(self, main_widget):
        QWidget.__init__(self)

        self.main_widget = main_widget # back-reference to be used sparingly
        buildDocumentWindow(self)
        layoutDocumentWindow(self)

        self.setWindowTitle('cryptography workbench')
        self.setGeometry(*Geometry.Document)
        self.setPalette(Colors.Palette)

    def keyPressEvent(self, event):
        if event.key() == ConfigOS.EscapeKey:
            self.main_widget.raise_()
